step = 3


def get_char(s, i):
    if i * step < len(s):
        # print(step * i, i, s[step * i])
        return s[step * i]
    else:
        p = step * i
        z = len(s) - 1
        r = p % z

        if r % 2 == 0:
            if r != 0:
                # print('d: ', r - 1, i, s[r - 1])
                return s[r - 1]
            else:
                # print('a: ', r + 1, i, s[r + 1])
                return s[r + 1]
        else:
            if r <= len(s) / 2:
                # print('t: ', r, i, s[r])
                return s[r]
            else:
                # print('r: ', r - 2, i, s[r - 2])
                return s[r - 2]


def load_data():
    with open("map.txt", "r") as d:
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
