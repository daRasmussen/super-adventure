with open('data.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]

def get_displacement():
    x, y = 0, 0
    # direcitons: N=0, E=1, S=2, W=3
    dir = 1
    for line in data:
        cmd, value = line[0], int(line[1:])
        if cmd == 'N' or (dir == 0 and cmd == 'F'):
            y += value
        elif cmd == 'S' or (dir == 2 and cmd == 'F'):
            y -= value
        elif cmd == 'E' or (dir == 1 and cmd == 'F'):
            x += value
        elif cmd == 'W' or (dir == 3 and cmd == 'F'):
            x -= value
        elif cmd == 'R':
            dir += value // 90
            dir = dir % 4
        elif cmd == 'L':
            dir -= value // 90
            dir = dir % 4
    return abs(x) + abs(y)


print(get_displacement())


