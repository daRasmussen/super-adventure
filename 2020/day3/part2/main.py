"""
This is main solution for day3 part 2 of
Advent of Code 2020
"""

"""
Takes lines and right and down, fills chars with found characters.
"""

fil_name = 'map.txt'


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
        elif target == limit:
            target = 0
        elif target < limit:
            break
    return target


def investigate(lines, right, down):
    row = 0
    chars = []
    while True:
        if down == 1:
            chars.append(down_one(lines, right, row))
        elif row > 1:
            target = int(row / down) if row % down == 0 else row
            if row != target:
                line = lines[row].strip()
                position = trim(target, len(line))
                print('row: ', row, 'target: ', target, 'length: ', len(line), 'position: ', position, 'char: ',
                      line[position])
                c = line[position]
                chars.append(c)
        row += 1
        if row == len(lines):
            break
    return chars


def load_data(right, down):
    with open(fil_name, "r") as d:
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


def in_range(number):
    return True if 2123550000 > number > 898425000 else False


def validate(search):
    re = fill_re(search, [])
    print('validates: ', re, multiply(re))
    print('in range: ', in_range(multiply(re)))
    return {
        're': re,
        'multiply': multiply(re)
    }


# 81675000 is to low
# 898425000 is to low

# 285862500  is fail
# 1388475000 is fail
# 1388475000 is fail
# 1143450000 is fail

# 2123550000 is to high
# 2246062500 is to high

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
validate(slopes)
ans = [2, 7, 3, 4, 2]
print('expected:  ', ans, multiply(ans))


def check2(number):
    failed = [
        81675000,
        898425000,
        285862500,
        1388475000,
        1388475000,
        1143450000,
        2123550000,
        2246062500,
    ]
    for nbr in failed:
        if nbr == number:
            print('The number: %d was found in list' % number)
        else:
            print('The number: %d was NOT found in list' % number)


check2(1592662500)
