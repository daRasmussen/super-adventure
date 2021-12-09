from aocd import submit, get_data
from math import ceil

data = get_data(day=19, year=2019)

def read_intcode() -> list:
    return list(map(int, data.split(",")))

class Intcode:

    def __init__(self, program: list):
        self.pc = 0
        self.relative_base = 0
        self.input_val = 0
        self.output = None
        self.stopped_on_input = False
        self.mem = [0] * 100000
        for pos, intcode in enumerate(program):
            self.mem[pos] = intcode

    def set_input(self, input_val: int):
        self.input_val = input_val

    def get_output(self):
        return self.output

    def run_until_input_or_done(self):
        return self.run(False, True)

    def run_until_io_or_done(self):
        return self.run(True, True)

    def run(self, stop_on_output=True, stop_on_input=False):
        self.stopped_on_input = False
        while True:
            opcode_obj = self._decode_opcode()
            opcode = opcode_obj[3] * 10 + opcode_obj[4]
            op1_mode = opcode_obj[2]
            op2_mode = opcode_obj[1]
            op3_mode = opcode_obj[0]
            if opcode == 1 or opcode == 2:
                op1, op2 = self._get_op1(op1_mode), self._get_op2(op2_mode)
                self.mem[self._get_op3_address(op3_mode, 3)] = op1 + op2 if opcode == 1 else op1 * op2
                self.pc += 4
            elif opcode == 3:
                self.mem[self._get_op3_address(op1_mode, 1)] = self.input_val
                self.pc += 2
                self.stopped_on_input = True
                if stop_on_input:
                    break
            elif opcode == 4:
                op1 = self._get_op1(op1_mode)
                self.output = op1
                self.pc += 2
                if stop_on_output:
                    break
            elif opcode == 5 or opcode == 6:
                op1, op2 = self._get_op1(op1_mode), self._get_op2(op2_mode)
                self.pc = op2 if (opcode == 5 and op1 != 0) or (opcode == 6 and op1 == 0) else self.pc + 3
            elif opcode == 7:
                op1, op2 = self._get_op1(op1_mode), self._get_op2(op2_mode)
                self.mem[self._get_op3_address(op3_mode, 3)] = 1 if op1 < op2 else 0
                self.pc += 4
            elif opcode == 8:
                op1, op2 = self._get_op1(op1_mode), self._get_op2(op2_mode)
                self.mem[self._get_op3_address(op3_mode, 3)] = 1 if op1 == op2 else 0
                self.pc += 4
            elif opcode == 9:
                self.relative_base += self._get_op1(op1_mode)
                self.pc += 2
            elif opcode == 99:
                break
            else:
                print('unknown opcode')
                break
        return self.output

    def _decode_opcode(self) -> list:
        opcode = self.mem[self.pc]
        digits = [0, 0, 0, 0, 0]
        pos = len(digits) - 1
        while opcode > 0 and pos >= 0:
            digits[pos] = opcode % 10
            opcode //= 10
            pos -= 1
        return digits

    def _get_op_address(self, mode, offset):
        if mode == 0:  # position mode
            return self.mem[self.pc + offset]
        if mode == 1:  # immediate mode
            return self.pc + offset
        if mode == 2:  # relative mode
            return self.relative_base + self.mem[self.pc + offset]

    def _get_op1(self, mode):
        return self.mem[self._get_op_address(mode, 1)]

    def _get_op2(self, mode):
        return self.mem[self._get_op_address(mode, 2)]

    def _get_op3_address(self, mode, offset):
        return self._get_op_address(mode, offset)

def gen_inputs(x1: int, x2: int, y1: int, y2: int) -> list:
    inputs = []
    for y in range(y1, y2):
        for x in range(x1, x2):
            inputs.append((x, y))
    return inputs


def gen_grid(width: int, height: int) -> list:
    grid = []
    for _ in range(0, height):
        grid.append(["."] * width)
    return grid

def serialize_grid(grid: list, width: int, height: int) -> str:
    return "\n".join(["".join([grid[y][x] for x in range(0, width)]) for y in range(0, height)])

def is_in_beam(program: list, x: int, y: int) -> bool:
    vm = Intcode(program)
    vm.set_input(x)
    vm.run_until_io_or_done()
    vm.set_input(y)
    vm.run_until_io_or_done()
    return vm.run_until_io_or_done() == 1

def find_right_edge(program: list, x: int, y: int) -> int:
    while True:
        if is_in_beam(program, x, y):
            break
        x -= 1
    return x

def get_slope(program: list) -> float:
    y = 10000
    x_right_edge = find_right_edge(program, 10000, y)
    return y / x_right_edge

def get_area_points(program: list, grid: list, inputs: list) -> int:
    offset = inputs[0]
    points = 0
    while len(inputs) > 0:
        x, y = inputs.pop(0)
        if is_in_beam(program, x, y):
            grid[y - offset[1]][x - offset[0]] = "#"
            points += 1
    return points

def part_one(width: int, height: int) -> int:
    program = read_intcode()
    grid = gen_grid(width, height)
    inputs = gen_inputs(0, width, 0, height)
    points = get_area_points(program, grid, inputs)
    print(serialize_grid(grid, width, height))
    return points

ans = part_one(50, 50)
#submit(ans, part='a', day=19, year=2019)

def binary_search(program: list, slope: float) -> int:
    y_low = 0
    y_high = 10000
    while y_low < y_high:
        y_mid = (y_high + y_low) // 2
        x_mid = find_right_edge(program, y_mid, y_mid) # search in square y_mid
        y_mid = ceil(x_mid * slope)
        if is_in_beam(program, x_mid - 99, y_mid + 99):
            y_high = y_mid
        else:
            y_low = y_mid + 1
    return find_right_edge(program, y_high, y_high)

def part_two() -> int:
    program = read_intcode()
    slope = get_slope(program)
    x = binary_search(program, slope)
    y = ceil(x * slope)
    return (x - 99) * 10000 + y

ans = part_two()

submit(ans, part='b', day=19, year=2019)
