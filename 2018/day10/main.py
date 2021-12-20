import re
from aocd import get_data

data = get_data(day=10, year=2018)

class Point():
    def __init__(self, pos_x, pos_y, vel_x, vel_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y
    def step(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y


HEIGHT = 10
WIDTH = 62

def run(s):
    points = []

    for line in s.split("\n"):
        (pos_x, pos_y, vel_x, vel_y) = re.findall(r"-?\d+", line)
        points.append(Point(int(pos_x), int(pos_y), int(vel_x), int(vel_y)))

    while True:
        y = []

        for point in points:
            point.step()
            y.append(point.pos_y)

        if max(y) - min(y) <= HEIGHT:
            return pprint(points)

def pprint(points):
    min_x = min(p.pos_x for p in points)
    min_y = min(p.pos_y for p in points)
    img = [[False for _ in range(HEIGHT)] for _ in range(WIDTH)]
    for p in points:
        img[p.pos_x - min_x][p.pos_y - min_y] = True

    result = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            if img[j][i]:
                result += "#"
            else:
                result += "."
        result += "\n"

    return result
print(run(data))
# submit(ans, part='a', day=10, year=2018)
# submit(ans, part='b', day=10, year=2018)
