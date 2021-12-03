import math


def _get_astriod_grid(file):
    grid = []
    with open(file) as f:
        for line in f.readlines():
            grid.append([x for x in line.strip()])
    return grid


def _find_asteroid_pos(astroid_map, width, height, x, y, dx, dy):
    pos_x = x + dx
    pos_y = y + dy
    while width > pos_x >= 0 and height > pos_y >= 0:
        if astroid_map[pos_y][pos_x] == "#":
            return tuple([pos_x, pos_y])
        pos_x += dx
        pos_y += dy
    return None

def _normalize(x, y):
    gcd = math.gcd(x, y)
    return tuple([x // gcd, y // gcd])

def _cmd_vector_angle(vector):
    hyp = math.sqrt(vector[0] * vector[0] + vector[1] * vector[1])
    return math.asin(vector[1] / hyp)

def _calc_quadrant_vectors(range_x, range_y, is_x_negative):
    dirs = set()
    for w in range_x:
        for h in range_y:
            if w == 0 and h == 0:
                continue
            dirs.add(_normalize(w, h))
    return sorted(dirs, key=_cmd_vector_angle, reverse=is_x_negative)

def _calc_vectors(width, height):
    sorted_dirs = []
    # Clockwise order: quadrant 1, 4, 3 and 2
    range_x = [range(0, width), range(0, width), range(-width, 0), range(-width, 0)]
    range_y = [range(-height, 0), range(0, height), range(0, height), range(-height, 0)]
    is_x_negative = [False, False, True, True]
    for quadrant in range(0, 4):
        sorted_dirs.extend(_calc_quadrant_vectors(range_x[quadrant], range_y[quadrant], is_x_negative[quadrant]))
    return sorted_dirs

def _get_monitoring_station_position(asteroid_grid):
    best_position = ([0,0])
    max_asteroids = 0
    width, height = len(asteroid_grid[0]), len(asteroid_grid)
    vectors = _calc_vectors(width, height)
    for y in range(0, height):
        for x in range(0, width):
            if asteroid_grid[y][x] == "#":
                count_asteroids = 0
                for vector in vectors:
                    pos = _find_asteroid_pos(asteroid_grid, width, height, x, y, vector[0], vector[1])
                    if pos is not None:
                        count_asteroids += 1
                if count_asteroids > max_asteroids:
                    max_asteroids = count_asteroids
                    best_position = ([x, y])
    return max_asteroids, best_position

# part 1
grid = _get_astriod_grid("data.txt")
r = _get_monitoring_station_position(grid)[0]
print(r)

# part 2
grid = _get_astriod_grid("data.txt")
width, height = len(grid[0]), len(grid)
vectors = _calc_vectors(width, height)
max_asteroids, station_pos = _get_monitoring_station_position(grid)
vaporized_count = 0
vaporized_target = 200
while vaporized_count < vaporized_target:
    for vector in vectors:
        asteroid_pos = _find_asteroid_pos(grid, width, height, station_pos[0], station_pos[1], vector[0], vector[1])
        if asteroid_pos is not None:
            grid[asteroid_pos[1]][asteroid_pos[0]] = "." # vaporized
            vaporized_count += 1
            if vaporized_count == vaporized_target:
                r = asteroid_pos[0] * 100 + asteroid_pos[1]
                print(r)
