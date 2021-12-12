from aocd import submit, get_data
from collections import defaultdict

data = get_data(day=4, year=2018)

lines = data.splitlines()
lines.sort()

def parseTime(line):
    words = line.split()
    _, time = words[0][1:], words[1][:-1]
    return int(time.split(":")[1])

C = defaultdict(int)
CM = defaultdict(lambda: defaultdict(int))
guard = None
asleep = False
for line in lines:
    time = parseTime(line)
    if "begins shift" in line:
        guard = int(line.split()[3][1:])
        asleep = None
    elif "falls asleep" in line:
        asleep = time
    elif "wakes up" in line:
        for t in range(asleep, time):
            CM[guard][t] += 1
            C[guard] += 1

def argmax(d):
    best = None
    for k, v in d.items():
        if best is None or v > d[best]:
            best = k
    return best

best_guard = argmax(C)
best_min = argmax(CM[best_guard])

ans = best_guard * best_min
print(ans)
submit(ans, part='a', day=4, year=2018)

# submit(ans, part='b', day=4, year=2018)
