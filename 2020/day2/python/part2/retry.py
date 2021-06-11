import re

with open("data.txt", "r") as data:
    valid = 0
    for line in data:
        pattern = r'(\d{1,2})-(\d{1,2})\s([a-z]):\s([a-z]+)'
        min_value, max_value, char, password = re.match(pattern, line).groups()
        print(min_value, max_value, char, password)
    print('valid: ', valid)
