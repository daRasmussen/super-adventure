"""
This is main solution for day4 part 1 of
Advent of Code 2020
"""

"""
Validate passport data, if it contains right number of keys.
Only key that could be missing is CID - Country Id
"""

import re

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
            if key == 'byr':
                byr = value.split(":")[1]
                if 1919 < int(byr) < 2003:
                    keys.append(key)
            if key == 'iyr':
                iyr = value.split(":")[1]
                if 2009 < int(iyr) < 2021:
                    keys.append(key)
            if key == 'eyr':
                eyr = value.split(":")[1]
                if 2019 < int(eyr) < 2031:
                    keys.append(key)
            if key == 'hgt':
                hgt = value.split(":")[1]
                unit = hgt[-2:]
                magnitude = int(hgt[:-2]) if hgt[:-2] else -1
                if unit == 'cm' and 149 < magnitude < 194:
                    keys.append(key)
                elif unit == 'in' and 58 < magnitude < 77:
                    keys.append(key)
            if key == 'hcl':
                hcl = value.split(":")[1]
                if re.search("#([a-f0-9]){6}", hcl):
                    keys.append(key)
            if key == 'ecl':
                ecl = value.split(":")[1]
                one = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                if ecl in set(one):
                    keys.append(key)
            if key == 'pid':
                pid = value.split(":")[1]
                if len(pid) == 9:
                    keys.append(key)
        diff = set(valid_keys).difference(keys)
        length = len(diff)
        if optional[0] in diff and length == 1 or length == 0:
            valid = valid + 1

    print('Number of valid passports are: ', valid)
