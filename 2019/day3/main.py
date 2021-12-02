from sys import maxsize

def get_wires(filename: str):
    with open(filename) as file:
        return (
            list(file.readline().strip().split(",")),
            list(file.readline().strip().split(","))
        )


def set_path(
        area: dict, 
        delay: dict, 
        wires: list,
        nbr: int, 
        set_delay: bool) -> int:
    distance = maxsize
    x, y = 0, 0
    count = 0
    for wire in range(len(wires)):
        prior = wires[wire]
        direction, steps = prior[0:1], int(prior[1:])
        max_steps = steps
        while max_steps > 0:
            if direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            elif direction == "U":
                y += 1
            elif direction == "D":
                y -= 1
            count += 1
            key = f"{x} {y}"
            if area.get(key) is None or area.get(key) == nbr:
                area[key] = nbr
                delay[key] = count
            else:
                distance = min(
                   distance,
                   delay[key] + count if set_delay else abs(x) + abs(y)
                )
            max_steps -= 1
    return distance

def get_distance(area, delay, wire1, wire2, set_delay):
    set_path(area, delay, wire1, 1, set_delay)
    return set_path(area, delay, wire2, 2, set_delay)

# part 1
filename = 'data.txt'
wire1, wire2 = get_wires(filename)
print(get_distance({}, {}, wire1, wire2, False))

# part 2 
print(get_distance({}, {}, wire1, wire2, True))

