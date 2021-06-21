# square = .
# tree = #

right = 3
down = 1
pos = [0, 0]


def get_char(string, index):
    if index < len(string):
        print('@index: ', index)
        return string[index]
    else:
        rest = int(index) % len(string) + 2
        print('@index: ', rest)
        # print('rest: ', rest, 'index: ', index, 'len: ', len(string))
        return string[rest]


def load_data():
    with open("test.txt", "r") as data:
        for line in data:
            pos[0] += right
            pos[1] += down
            yield get_char(line, pos[0])


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
