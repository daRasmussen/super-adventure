from parse import parse
from aocd import submit, get_data

data = get_data(day=23, year=2018)
ans = ''

X, Y, Z, RANGE = 0, 1, 2, 3
ORIGIN = (0, 0, 0, 0)


def part1(bots):
    # find the nanobot with the largest range
    strongest = max(bots, key=lambda bot: bot[RANGE])
    distances = [manhattan(bot, strongest) for bot in bots]

    # number of nanobots in range of the strongest nanobot
    return len([d for d in distances if d <= strongest[RANGE]])

def manhattan(a, b):
    (x1, y1, z1, _), (x2, y2, z2, _) = a, b
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


def _parse(lines):
    # list of tuples (x, y, z, range)
    return [tuple(parse("pos=<{:d},{:d},{:d}>, r={:d}", line)) for line in lines]


ans = part1(_parse(data.splitlines()))
submit(ans, part='a', day=23, year=2018)
# submit(ans, part='b', day=23, year=2018)
