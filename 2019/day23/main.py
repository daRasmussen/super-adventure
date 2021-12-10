from aocd import submit, get_data

data = get_data(day=23, year=2019)

def read_intcode() -> list:
    return [int(x) for x in data.split(",")]

class NAT:
    def __init__(self, network):
        self.network = network
        self.packet = None
        self.last_y_delivered = None

    def is_network_idle(self):
        for computer in self.network:
            if not computer.idle:
                return False
        return True

    def has_packet(self):
        return self.packet is not None

    def is_repeated_y(self):
        return self.packet[1] == self.last_y_delivered

    def send_packet(self):
        self.last_y_delivered = self.packet[1]
        self.network[0].packet_queue.append(self.packet)
        self.packet = None

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

class NetIntcode:

    def __init__(self, program: list, address: int, target_address: int, network: list):
        self.packet_queue = []
        self.vm = Intcode(program)
        self.vm.input_val = address
        self.target_address = target_address
        self.network = network
        self.vm.run_until_input_or_done()
        self.vm.input_val = -1
        self.idle = False

    def run_until_io(self) -> int or None:
        if not self.packet_queue:
            self.vm.input_val = -1
        else:
            self.vm.input_val = self.packet_queue[0][0]  # provide X from next packet
        output = self.vm.run_until_io_or_done()
        if self.vm.stopped_on_input:
            if self.packet_queue:
                x, y = self.packet_queue.pop(0)
                self.vm.input_val = y
                self.vm.run_until_input_or_done()
            else:
                self.idle = True
        else:
            self.idle = False
            dest_address = output
            x = self.vm.run_until_io_or_done()
            y = self.vm.run_until_io_or_done()
            if dest_address == self.target_address:
                return dest_address, x, y
            self.network[dest_address].packet_queue.append((x, y))

def init_network(program: list, num_computers: int, nat_address: int) -> list:
    network = []
    for address in range(num_computers):
        network.append(NetIntcode(program, address, nat_address, network))
    return network

def part_one(num_computers: int, target_address: int) -> int:
    network = init_network(read_intcode(), num_computers, target_address)
    while True:
        for computer in network:
            packet = computer.run_until_io()
            if packet is not None and packet[0] == target_address:
                return packet[2] # Y value

ans = part_one(50, 255)
submit(ans, part='a', day=23, year=2019)

# submit(ans, part='b', day=23, year=2019)
