import math

right = 3


def get_char(s, y):
    if y * right < len(s):
        return s[right * y]
    else:
        p = right * y
        q = math.floor(y / right)
        z = len(s) - 1
        return s[p - q * z]


def load_data():
    with open("test.txt", "r") as data:
        for line, index in data:
            yield get_char(line.strip(), index)


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
