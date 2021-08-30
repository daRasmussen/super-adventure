import unittest

import getopt
import sys

target = 'shiny gold'


def run(path):
    print('RUN', path)
    db = {}
    with open(path, "r") as data:
        res = []
        res2 = []
        lines = data.readlines()
        for index, line in enumerate(lines):
            bags_inside = [x for x in line.split("contain")[1] if not x.isdigit() if not x == "."]
            raw_colors = [
                x for x in "".join(bags_inside).strip().split(" ")
            ]
            db[index] = {
                'line ' + str(index + 1): line,
                'color': " ".join(line.split(" ")[0:2]),
                'contains': {
                    'text': "".join(bags_inside).strip(),
                    'raw_colors': raw_colors,
                    'colors': [
                        x.replace(", ", "").replace("s ", "").strip() for x in " ".join(raw_colors).split("bag")
                        if not x == ''
                    ]
                }
            }
        for key, value in db.items():
            color = value["color"]
            contains_colors = value["contains"]["colors"]
            for contain_color in contains_colors:
                if contain_color == target:
                    if res.count(color) == 0:
                        res.append(color)
        for key, value in db.items():
            color2 = value["color"]
            contains_colors2 = set([x for x in value["contains"]["colors"] if not x == 's'])
            # bright white and muted yellow
            print(not set(res).difference(contains_colors2))
            if not set(res).difference(contains_colors2):
                print(res)
                print(contains_colors2)
                if res.count(color) == 0:
                    res2.append(color2)
        # 19
        # 14
        # 49
        # 576
        print(res, res2)
        print(len(res) + len(res2))
        return len(res + res2)


class Cases(unittest.TestCase):
    def test(self):
        self.assertEqual(4, run('test.txt'))


def main1():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ht:v:", ["help", "tests", "verbose"])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
    verbose = False
    tests = False
    for o, a in opts:
        if o in ("-v", "--verbose"):
            verbose = a if a else True
            print('Verbose is: ', verbose)
        elif o in ("-h", "--help"):
            print('main.py -v <bool>')
            print('main.py -t <bool>')
            print('main.py -h')
            print('main.py --verbose')
            print('main.py --tests')
            print('main.py --help')
            sys.exit()
        elif o in ("-t", '--tests'):
            tests = a if a else True
            if tests:
                run('test.txt')
            sys.exit()
    run('data.txt')
    unittest.main()


if __name__ == '__main__':
    main1()
