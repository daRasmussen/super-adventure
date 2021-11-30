with open('data.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]

def to_binay(dec : int):
    bits = []
    while dec != 0:
        bits.append(str(dec%2))
        dec = dec // 2
    bits.reverse()
    s = ''
    s = s.join(bits)
    
    while len(s) != 36:
        s = '0' + s
    return s

def to_decimal(b):
    while b[0] == '0':
        b = b[1:]

    dec = 0
    for i in range(len(b)):
        j = len(b) - i - 1
        dec += int(b[j]) * (2**i)

    return dec


def get_mem_total():
    mem = {}
    mask = ''

    for line in data:
        line = line.split(" = ")
        if 'mask' in line[0]:
            mask = line[1]
        else:
            loc = line[0][4:-1]
            value = int(line[1])
            value_binary = list(to_binay(value))
            # apply the mask
            for i in range(len(mask)):
                if mask[i] != 'X':
                    value_binary[i] = mask[i]
            masked_string = ''
            masked_string = masked_string.join(value_binary)
            masked_num = to_decimal(masked_string)
            mem[loc] = masked_num
    total = 0
    for i in mem.values():
        total += i
    return total

print(get_mem_total())
