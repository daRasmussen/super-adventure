"""
This is a docstring in python
"""


def translate(nbr):
    return nbr - 1


"""
This is a docstring in python
"""


def investigate(lines, right, down):
    index = 0
    chars = []
    while True:
        if down == 1:
            p = right * index
        elif down != 1:
            p = right * index
        line = lines[down].strip()
        z = len(line)
        r = p % z
        chars.append(line[r])
        index += 1
        if index == len(lines):
            break
    return chars


def load_data(right, down):
    with open("test.txt", "r") as d:
        yield investigate(d.readlines(), right, down)


def find_trees(r, d):
    trees = 0
    for chars in load_data(r, d):
        for c in chars:
            if c == '#':
                trees += 1
    return trees


def fill_re(search, re):
    for s in search:
        right, down = s
        re.append(find_trees(right, down))
    return re


def multiply(arr):
    s = 1
    for v in arr:
        s *= v
    return s


def validate(search):
    re = fill_re(search, [])
    print('validates: ', re, multiply(re))
    return {
        're': re,
        'multiply': multiply(re)
    }


slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
print(fill_re([[1, 1]], [])[0])
validate(slopes)
# print('Validate: ', validate([[1, 1]]))
ans = [2, 7, 3, 4, 2]
print('expected:  ', ans, multiply(ans))
