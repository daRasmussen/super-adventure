"""
This is main solution for day4 part 1 of
Advent of Code 2020
"""

"""
Validate passport data, if it contains right number of keys.
Only key that could be missing is CID - Country Id
"""

file_name = "data.txt"

valid_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
optional = ['cid']

with open(file_name, "r") as d:
    valid = 0
    lines = list(map(lambda line: [] if line == '\n' else line.strip(), d))
    passports = []
    tmp = []
    for item in lines:
        if type(item) == str:
            tmp = tmp + [item]
        else:
            passports.append(" ".join(filter(None, tmp)))
            tmp = []
    for passport in passports:
        values = passport.split(" ")
        keys = []
        for value in values:
            key = value.split(":")[0]
            keys.append(key)
        diff = set(valid_keys).difference(keys)
        length = len(diff)
        if optional[0] in diff and length == 1 or length == 0:
            valid = valid + 1
        # print('Following keys: ', keys, ' are compared to: ', valid_keys)
    print('Number of valid passports are: ', valid)
