import re
from aocd import get_data, submit

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
def run(s):
    points = []

    for line in s.split("\n"):
        (pos_x, pos_y, vel_x, vel_y) = re.findall(r"-?\d+", line)
        points.append(Point(int(pos_x), int(pos_y), int(vel_x), int(vel_y)))

    seconds = 0

    while True:
        y = []

        for point in points:
            point.step()
            y.append(point.pos_y)

        seconds += 1

        if max(y) - min(y) <= HEIGHT:
            return seconds
ans = run(data)
print(ans)
submit(ans, part='b', day=10, year=2018)
