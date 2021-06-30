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


def trim(target, limit):
    while True:
        if target > limit:
            target = target - limit
        if target <= limit:
            break
    return target


def investigate(lines, right, down):
    row = 0
    chars = []
    if down > 1:
        chars.append('.')
        chars.append('.')
    while True:
        if down == 1:
            chars.append(down_one(lines, right, row))
        elif row > 1:
            target = int(row / down) if row % down == 0 else row
            if row != target:
                line = lines[row]
                position = trim(target, len(line) - 1)
                c = line[position]
                chars.append(c)
            else:
                chars.append('.')
        row += 1
        if row == len(lines):
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


def inRange(number):
    return True if 898425000 > number > 2123550000 else False


def validate(search):
    re = fill_re(search, [])
    print('validates: ', re, multiply(re))
    print('in range: ', inRange(multiply(re)))
    return {
        're': re,
        'multiply': multiply(re)
    }


# 81675000 is to low
# 898425000 is to low

# 285862500  is fail
# 1388475000 is fail
# 1388475000 is fail


# 2123550000 is to high
# 2246062500 is to high

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
validate(slopes)
ans = [2, 7, 3, 4, 2]
print('expected:  ', ans, multiply(ans))
