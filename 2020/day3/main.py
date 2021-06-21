# square = .
# tree = #

right = 3
down = 1
pos = [0, 0]


def load_data():
    with open("sandbox.txt", "r") as data:
        for line in data:
            pos[0] += right
            pos[1] += down
            print(pos)
            if pos[0] - 1 < len(line):
                yield line[pos[0]]
            elif pos[0] > len(line):
                yield line[-1]
            elif len(line) == 0:
                break


def validate():
    squares = 0
    trees = 0
    for c in load_data():
        print(c)
        if c == '.':
            squares += 1
        elif c == '#':
            trees += 1

    print('squares: ', squares, 'trees: ', trees)


validate()
