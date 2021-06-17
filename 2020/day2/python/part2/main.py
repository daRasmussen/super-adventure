import re


def load_data():
    with open("data.txt", "r") as data:
        for line in data:
            pattern = r'(\d{1,2})-(\d{1,2})\s([a-z]):\s([a-z]+)'
            min_, max_, char, password = re.match(pattern, line).groups()
            yield int(min_) - 1, int(max_) - 1, char, list(password)


def validate():
    valid = 0
    for min_, max_, char, password in load_data():
        if password[min_] == char:
            if password[max_] != char:
                valid = valid + 1
        if password[max_] == char:
            if password[min_] != char:
                valid = valid + 1
    print('valid: ', valid)


validate()
