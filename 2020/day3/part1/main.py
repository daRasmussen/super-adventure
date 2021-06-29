step = 1


def get_char(s, i):
    p = step * i
    z = len(s)
    r = p % z
    return s[r]


def load_data():
    with open("test.txt", "r") as d:
        for index, line in enumerate(d):
            yield get_char(line.strip(), index)


def validate():
    squares = -1
    trees = 0
    for c in load_data():
        if c == '.':
            squares += 1
        elif c == '#':
            trees += 1
    print(trees)


validate()
