def read_intcode(file):
    with open(file) as f:
        return list(map(int, f.read().split(",")))

def decode_opcode(num):
    digits = [0] * 5
    pos = len(digits) - 1
    while num > 0  and pos >= 0:
        digits[pos] = num % 10
        num //= 10
        pos -= 1
    return digits

def get_op1(program, pc, mode):
    return program[program[pc + 1]] if mode == 0 else program[pc + 1]

def get_op2(program, pc, mode):
    return program[program[pc + 2]] if mode == 0 else program[pc + 2]

def run(program, inputs, is_feedback=False, pc=0):
    diagnostic = 0
    pc = pc
    while pc < len(program):
        code_obj = decode_opcode(program[pc])
        code = code_obj[3] * 10 + code_obj[4]
        op1_mode, op2_mode = code_obj[2], code_obj[1]
        if code == 1 or code == 2:
            op1, op2 = get_op1(program, pc, op1_mode), get_op2(program, pc, op2_mode)
            dest = program[pc + 3]
            program[dest] = op1 + op2 if code == 1 else op1 * op2
            pc += 4
        elif code == 3:
            if len(inputs) == 0:
                raise Exception("no inputs, ex. data.txt!")
            program[program[pc + 1]] = inputs.pop(0)
            pc += 2
        elif code == 4:
            op1 = get_op1(program, pc, op1_mode)
            diagnostic = op1
            pc += 2
            if is_feedback:
                return diagnostic, pc
        elif code == 5 or code == 6:
            op1, op2 = get_op1(program, pc, op1_mode), get_op2(program, pc, op2_mode)
            pc = op2 if (code == 5 and op1 != 0) or (code == 6 and op1 == 0) else pc + 3
        elif code == 7:
            op1, op2 = get_op1(program, pc, op1_mode), get_op2(program, pc, op2_mode)
            program[program[pc + 3]] = 1 if op1 < op2 else 0
            pc += 4
        elif code == 8:
            op1, op2 = get_op1(program, pc, op1_mode), get_op2(program, pc, op2_mode)
            program[program[pc + 3]] = 1 if op1 == op2 else 0
            pc += 4
        elif code == 99:
            if is_feedback:
                return diagnostic, None
            break
        else:
            print("unkown opcode")
            break
    return diagnostic

def get_phase_permutations(phases):
    phase_perms = [[]]
    for n in phases:
        new_perm = []
        for perm in phase_perms:
            for i in range(len(perm)+1):
                new_perm.append(perm[:i] + [n] + perm[i:])
                phase_perms = new_perm
    return phase_perms

# part 1
max_thrust_signal = 0
program = read_intcode("data.txt")
phase_perms = get_phase_permutations(range(0, 5))
for phase_perm in phase_perms:
    output = 0
    while len(phase_perm) > 0:
        output = run(program.copy(), [phase_perm.pop(0), output])
    max_thrust_signal = max(max_thrust_signal, output)
print(max_thrust_signal)
