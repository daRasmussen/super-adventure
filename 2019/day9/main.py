def _decode_opcode(num):
    digits = [0] * 5
    pos = len(digits) - 1
    while num > 0 and pos >= 0:
        digits[pos] = num % 10
        num //= 10
        pos -= 1
    return digits

def _get_op_address(program, pc, mode, offset, rel_base):
    if mode == 0: # position mode
        return program[pc + offset]
    if mode == 1: # immeditate mode
        return pc + offset
    if mode == 2: # relative mode 
        return rel_base + program[pc + offset]

def _get_op1(program, pc, mode, rel_base):
    return program[_get_op_address(program, pc, mode, 1, rel_base)]

def _get_op2(program, pc, mode, rel_base):
    return program[_get_op_address(program, pc, mode, 2, rel_base)]

def _get_op3_address(program, pc, mode, offset, rel_base):
    return _get_op_address(program, pc, mode, offset, rel_base)

def get_data(file):
    with open(file) as f:
        return list(map(int, f.read().split(",")))

def run(program, input_id=0):
    diagnostic = 0
    pc = 0
    rel_base = 0
    mem = [0] * 100000
    for pos, intcode in enumerate(program):
        mem[pos] = intcode
    while pc < len(program):
        code_obj = _decode_opcode(mem[pc])
        code = code_obj[3] * 10 + code_obj[4]
        op1_mode = code_obj[2]
        op2_mode = code_obj[1]
        op3_mode = code_obj[0]
        if code == 1 or code == 2:
            op1, op2 = _get_op1(mem, pc, op1_mode, rel_base), _get_op2(mem, pc, op2_mode, rel_base)
            mem[_get_op3_address(mem, pc, op3_mode, 3, rel_base)] = op1 + op2 if code == 1 else op1 * op2
            pc += 4
        elif code == 3:
            mem[_get_op3_address(mem, pc, op1_mode, 1, rel_base)] = input_id
            pc += 2
        elif code == 4:
            op1 = _get_op1(mem, pc, op1_mode, rel_base)
            diagnostic = op1
            pc += 2
        elif code == 5 or code == 6:
            op1, op2 = _get_op1(mem, pc, op1_mode, rel_base), _get_op2(mem, pc, op2_mode, rel_base)
            pc = op2 if (code == 5 and op1 != 0) or (code == 6 and op1 == 0) else pc + 3
        elif code == 7:
            op1, op2 = _get_op1(mem, pc, op1_mode, rel_base), _get_op2(mem, pc, op2_mode, rel_base)
            mem[_get_op3_address(mem, pc, op3_mode, 3, rel_base)] = 1 if op1 < op2 else 0
            pc += 4
        elif code == 8:
            op1, op2 = _get_op1(mem, pc, op1_mode, rel_base), _get_op2(mem, pc, op2_mode, rel_base)
            mem[_get_op3_address(mem, pc, op3_mode, 3, rel_base)] = 1 if op1 == op2 else 0
            pc += 4
        elif code == 9:
            rel_base += _get_op1(mem, pc, op1_mode, rel_base)
            pc += 2
        elif code == 99:
            break
        else:
            print("unknown opcode")
            break
    return diagnostic

# part 1
r = run(get_data("data.txt"), 1)
print(r)

# part 2
r = run(get_data("data.txt"), 2)
print(r)
