with open("data.txt") as f:
    d = f.readlines()
    instructions = [x.strip() for x in d]

pos = 0
dep = 0
for instruction in instructions:
    cmd, val = instruction.split(" ")
    val = int(val)
    if cmd == "forward":
        pos += val
    if cmd == "down":
        dep += val
    if cmd == "up":
        dep -= val
print(pos * dep)

# part 2
aim = 0
pos = 0
dep = 0
for instruction in instructions:
    cmd, val = instruction.split(" ")
    val = int(val)
    if cmd == "forward":
        pos += val
        dep += aim * val
    if cmd == "down":
        aim += val
    if cmd == "up":
        aim -= val
print(pos * dep)



