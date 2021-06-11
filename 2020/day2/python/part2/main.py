import re


def fix(index, password):
    arr = list(password)
    last = len(arr)
    if 0 <= index < last:
        if index == 0:
            return index + 1
        elif index == last:
            return index - 1
        else:
            return index
    else:
        return False


def magic(c, p, v):
    for i in enumerate(c):
        index, value = i
        if int(v[0]) - 1 <= int(index) <= int(v[0]) or int(v[1]) - 1 <= int(index) <= int(v[1]):
            return p[index] == value


def check(o):
    c = []
    for i, x in enumerate(list(o["password"])):
        if x == o["charSet"]:
            c.append({
                'index': fix(i, o["password"]),
                'value': x
            })
    if 0 == len(c) == 1:
        return True
    else:
        return magic(
            c,
            list(o["password"]),
            [
                o['min'],
                o['max']
            ]
        )


def find(exp, arg):
    return re.findall(exp, arg)

# Unfinished
with open("data.txt", "r") as data:
    valid = 0
    for line in data:
        min_max, char_set, password = re.split('\\s+', line.strip())
        minimum, maximum = find('[0-9]+', min_max)
        char_set = char_set[:-1]
        valid = valid + 1 if check({
            "min": minimum,
            "max": maximum,
            "charSet": char_set,
            "password": password
        }) else valid + 0
    print('valid: ', valid)
