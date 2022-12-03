with open('data.txt') as f:
    bits = f.read().strip().split("\n")
g = []
e = []
while len(g) < len(bits[0]):
    t = []
    for bit in bits:
        target = bit[len(g)]
        t.append(target)
    o = [b for b in t if b == '1']
    z = [b for b in t if b == '0']
    g.append('0' if len(z) > len(o) else '1')
    e.append('1' if len(z) > len(o) else '0')

gamma = int("".join(g), 2)
epsilon = int("".join(e), 2)
power = gamma * epsilon
print(power)

# part 2
test = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]
def filter_ones(bits, index):
    if len(bits) == 1:
        return bits
    else:
        ones, zeros= [], []
        for bit in bits:
            if bit[index] == '0':
                zeros.append(bit)
            if bit[index] == '1':
                ones.append(bit)
        index += 1
        if len(ones) > len(zeros):
            return filter_ones(ones, index)
        elif len(ones) < len(zeros):
            return filter_ones(zeros, index)
        elif len(ones) == len(zeros):
            return filter_ones(ones, index)
def filter_zeros(bits, index):
    if len(bits) == 1:
        return bits
    else:
        ones, zeros= [], []
        for bit in bits:
            if bit[index] == '0':
                zeros.append(bit)
            if bit[index] == '1':
                ones.append(bit)
        index += 1
        if len(ones) > len(zeros):
            return filter_zeros(zeros, index)
        elif len(ones) < len(zeros):
            return filter_zeros(ones, index)
        elif len(ones) == len(zeros):
            return filter_zeros(zeros, index)


o = filter_ones(test, 0)
c = filter_zeros(test, 0)
o = int(o[0], 2)
c = int(c[0], 2)
print(o, c, o * c)

ox = filter_ones(bits, 0)
co = filter_zeros(bits, 0)
ox = int(ox[0], 2)
co = int(co[0], 2)
life = ox * co
print(life)
        


