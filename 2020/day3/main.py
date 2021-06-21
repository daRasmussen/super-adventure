import math

step = 3


def get_char(s, i):
    if i * step < len(s):
        return s[step * i]
    else:
        p = step * i
        q = math.floor(i / step)
        z = len(s) - 1
        return s[p - q * z]


def load_data():
    with open("test.txt", "r") as d:
        for index, line in enumerate(d):
            yield get_char(line.strip(), index)


def validate():
    squares = 0
    trees = 0
    for c in load_data():
        if c == '.':
            squares += 1
        elif c == '#':
            trees += 1

    print('squares: ', squares, 'trees: ', trees)


validate()
