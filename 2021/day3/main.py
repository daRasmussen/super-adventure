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

