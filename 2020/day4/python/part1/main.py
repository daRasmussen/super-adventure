"""
This is main solution for day4 part 1 of
Advent of Code 2020
"""

"""
Validate passport data, if it contains right number of keys.
Only key that could be missing is CID - Country Id
"""

import uuid

file_name = "test.txt"

valid_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
pps = {}
passport = []


def check_passport(ud, passport_as_list):
    """ Takes a list of passport keys and values, and checks each key if that key is in valid_keys. Returns tuple
     with uuid is valid true or false."""
    is_valid = False
    return ud, is_valid


with open(file_name, "r") as d:
    print(check_passport('test', []))
    for l in d:
        line = l.strip().split()
        if not len(line) == 0:
            passport += line
        else:
            pps[uuid.uuid4()] = passport
            passport = []
    if not len(passport) == 0:
        pps[uuid.uuid4()] = passport
        passport = []
    res = {}
    for uuid, pp_as_list in pps.items():
        res += check_passport(uuid, pp_as_list)
        print(res)
    print(len(res))
