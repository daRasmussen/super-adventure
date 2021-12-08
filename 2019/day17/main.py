from aocd import submit, get_data
from collections import defaultdict

data = get_data(day=17, year=2019)

def read_intcode():
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

    def run_until_input_or_done(self) -> int:
        return self.run(False, True)

    def run_until_io_or_done(self) -> int:
        return self.run(True, True)

    def run(self, stop_on_output=True, stop_on_input=False) -> int or None:
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
                return
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

    def _get_op_address(self, mode, offset) -> int:
        if mode == 0:  # position mode
            return self.mem[self.pc + offset]
        if mode == 1:  # immediate mode
            return self.pc + offset
        if mode == 2:  # relative mode
            return self.relative_base + self.mem[self.pc + offset]

    def _get_op1(self, mode) -> int:
        return self.mem[self._get_op_address(mode, 1)]

    def _get_op2(self, mode) -> int:
        return self.mem[self._get_op_address(mode, 2)]

    def _get_op3_address(self, mode, offset) -> int:
        return self._get_op_address(mode, offset)

def is_intersection(grid: dict, x: int, y: int, width: int, height: int) -> bool:
    if x == 0 or y == 0 or x == width - 1 or y == height - 1:
        return False
    return grid[(x - 1, y)] == ord('#') and grid[(x + 1, y)] == ord('#') \
           and grid[(x, y - 1)] == ord('#') and grid[(x, y + 1)] == ord('#')


def is_grid_char(num: int) -> bool:
    chars = set('#.^v<>')
    return str(chr(num)) in chars or num == 10  # newline


def get_grid(vm: Intcode) -> (dict, int, int):
    grid = {}
    x, y, width, height = 0, 0, 0, 0
    output = vm.run()
    while output is not None:
        if not is_grid_char(output):
            break
        if output == 10:  # newline
            y += 1
            width = max(width, x)
            x = 0
        else:
            grid[(x, y)] = output
            x += 1
        output = vm.run()
    height = y - 1  # input.txt.txt ends with newline
    return grid, width, height


def get_alignment_param_sum(grid: dict, width: int, height: int) -> int:
    alignment_param_sum = 0
    for y in range(0, height):
        for x in range(0, width):
            if grid[(x, y)] == 35 and is_intersection(grid, x, y, width, height):
                alignment_param_sum += x * y
    return alignment_param_sum


def serialize_grid(grid: dict, width: int, height: int):
    return '\n'.join([''.join(map(chr, [grid[(x, y)] for x in range(0, width)])) for y in range(0, height)])


def part_one() -> int:
    vm = Intcode(read_intcode())
    grid, width, height = get_grid(vm)
    return get_alignment_param_sum(grid, width, height)

ans = part_one()
#submit(ans, part="a", day=17, year=2019)

def string_to_ascii_list(string: str) -> list:
    return list(map(ord, list(string)))


def get_collected_dust(vm: Intcode) -> int:
    # This is obtained from inspecting the robot path (grid)
    input_routine = string_to_ascii_list('A,B,B,A,C,A,C,A,C,B\n'
                                         'L,6,R,12,R,8\n'
                                         'R,8,R,12,L,12\n'
                                         'R,12,L,12,L,4,L,4\n'
                                         'n\n')
    while True:
        if len(input_routine) > 0:
            vm.set_input(input_routine.pop(0))
        output = vm.run_until_input_or_done()
        if output is None:
            collected_dust = vm.get_output()
            break
    return collected_dust


def part_two() -> int:
    program = read_intcode()
    program[0] = 2
    vm = Intcode(program)
    grid, width, height = get_grid(vm)
    print(serialize_grid(grid, width, height))
    return get_collected_dust(vm)

print('\n')
ans = part_two()
submit(ans, part="b", day=17, year=2019)
