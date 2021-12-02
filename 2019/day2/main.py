with open('data.txt') as f:
    d = f.readlines()
    d = [x.strip() for x in d]
    li = d[0].split(",")
    li = [int(x) for x in li]
    li[1] = 12
    li[2] = 2
t= []
for l in li:
    if len(t) != 4:
        t.append(l)
        if len(t) == 4:
            i, a, b, o = t[0], t[1], t[2], t[3]
            if i == 1:
                li[o] = li[a] + li[b]
            if i == 2:
                li[o] = li[a] * li[b]
            if i == 99:
                break
    else:
        t = [l]
print(li[0])

# part 2
def run_program(program: list, noun: int, verb: int) -> int:
    program[1] = noun
    program[2] = verb 
    pc = 0
    while pc < len(program):
        opcode = program[pc]
        op1 = program[program[pc + 1]]
        op2 = program[program[pc + 2]]
        dest = program[pc + 3]
        if opcode == 1 or opcode == 2:
            program[dest] = op1 + op2 if opcode == 1 else op1 * op2
            pc += 4
        elif opcode == 99:
            break
        else:
            print('unkown opcode')
            break
    return program[0]

with open('data.txt') as f:
    d = f.readlines()
    d = [x.strip() for x in d]
    li = d[0].split(",")
    li = [int(x) for x in li]
t = 19690720
for noun in range(100):
    for verb in range(100):
        if run_program(li.copy(), noun, verb ) == t:
            print(100 * noun + verb)
