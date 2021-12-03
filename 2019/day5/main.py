data = []
with open("data.txt") as f:
    data = [int(x) for x in f.read().split(",")]

def get_parameter_modes(op):
    # the first parameter's mode is in the hundrets digit.
    mode1 = (op // 100) % 10
    # the second parameter's mode is in the thousands digit.
    mode2 = (op // 1000) % 10
    # the third parameter's mode is in the ten-thousands digit. 
    mode3 = (op // 10000) % 10
    return [mode1, mode2, mode3]

position_mode = 0
intermediate_mode = 1
def run(d):
    pc = 0
    output = [0]
    success = True
    while pc < len(d):
        opsize = 4
        op = d[pc]
        [mode1, mode2, mode3] = get_parameter_modes(op)
        op = op % 100
        if op == 99: # halt
            opsize = 1
            return [success, output[-1]]
        elif op == 1: # add
            # opsize = 4
            [addr1, addr2, outAddr] = d[pc+1:pc+4]
            v1 = addr1 if mode1 == position_mode else d[addr1]
            v2 = addr2 if mode2 == position_mode else d[addr2]
            v3 = outAddr if mode3 == position_mode else d[outAddr]
            d[v3] = v1 + v2
        elif op == 2: # multiply
            # opsize = 4
            [addr1, addr2, outAddr] = d[pc+1:pc+4]
            v1 = 0
            v2 = 0
            v3 = 0
            if mode1 == position_mode:
                v1 = d[addr1]
            else:
                v1 = addr1
            if mode2 == position_mode:
                v2 = d[addr2]
            else:
                v2 = addr2
            v3 = outAddr if mode3 == position_mode else d[outAddr]
            d[v3] = v1 * v2
        elif op == 3: # store
            addr1 = d[pc+1]
            v1 = addr1 if mode1 == 0 else d[addr1]
            opsize = 2  # op + address
            d[v1] = 1
        elif op == 4: #retrive
            addr1 = d[pc+1]
            v1 = addr1 if mode1 == 0 else d[addr1]
            opsize = 2
            val = d[v1]
            output.append(val)
            if val != 0:
                print(f"failure! {val}")
                success = False
            else:
                print(val)
        else:
            print(f"unknown op: {op} at pc: {pc}")
            return [False, 999]
        pc += opsize
    return 0

r = run(data)
print(r)
