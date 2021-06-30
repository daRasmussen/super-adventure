"""
This is main solution for day3 part 2 of
Advent of Code 2020
"""

"""
Takes lines and right and down, fills chars with found characters.
"""


def down_one(lines, right, index):
    line = lines[index].strip()
    p = right * index
    z = len(line)
    r = p % z
    return line[r]


def down_x(lines, right, index, down):
    # print('index: ', index, 'down: ', down)
    print(index * down, (index * down) / down)
    line = lines[down].strip()
    p = right * down
    z = len(line)
    r = p % z
    return line[r]


def investigate(lines, right, down):
    index = 0
    chars = []
    count = 0
    while True:
        if down == 1:
            chars.append(down_one(lines, right, index))
        else:
            count += 1
            if count == down:
                line = lines[index].strip()
                p = right - 1
                z = len(line)
                r = p % z
                chars.append(line[r])
                count = 0
        index += 1
        if index == len(lines):
            break
    return chars


def load_data(right, down):
    with open("map.txt", "r") as d:
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


# 81 675 000 is to low
# 898 425 000 is to low

# 2 123 550 000 is to high
# 2 246 062 500 is to high

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
validate(slopes)
ans = [2, 7, 3, 4, 2]
print('expected:  ', ans, multiply(ans))
