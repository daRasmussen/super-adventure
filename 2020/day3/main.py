import math

step = 3

def get_char(s, i):
    if i * step < len(s):
        print(step * i, i, s[step * i])
        return s[step * i]
    else:
        p = step * i
        q = math.floor(p / len(s))
        z = len(s) - 1
        r = p % z
        c = math.floor(i / step)

        # print(r, i, s[r], c)
        # return s[r]

        if r % 2 == 0:
            print(r - 1, i, s[r - 1], c)
            return s[r - 1]
        else:
            print(r, i, s[r], c)
            return s[r]

# calc index
# calc x and y pos ...
# pos x = row * step

# get_char takes a index
# returns s[i]
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
