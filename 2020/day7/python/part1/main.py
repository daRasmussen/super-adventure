import unittest

import getopt
import sys

target = 'shiny gold'


def run(path):
    print('RUN', path)
    db = {}
    with open(path, "r") as data:
        res = []
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
                    'colors': [x.replace(', ', '').strip() for x in " ".join(raw_colors).split("bags") if not x == '']
                }
            }
        for key, value in db.items():
            color = value["color"]
            contains_colors = value["contains"]["colors"]

            for contain_color in contains_colors:
                if contain_color == target:
                    if len(res) == 0:
                        res.append(color)
                    elif res.count(color) == 0:
                        res.append(color)
            # for key, value in db.items():
            #     color2 = value["color"]
            #     contains_colors2 = "".join(value["contains"]["raw_colors"])
            #     for contain_color2 in contains_colors2:
            #         for res_color in res:
            #             if contain_color2 == res_color:
            #                 if res.count(color2) == 0:
            #                     res.append(color2)
        # 19
        # 14
        # 576
        print(res)
        print(len(res))
        return len(res)


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
