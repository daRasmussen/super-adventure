import unittest

import getopt
import sys


def run(path):
    print('RUN', path)
    with open(path, "r") as data:
        lines = data.readlines()
        print(lines)
    return path


class Cases(unittest.TestCase):
    def test(self):
        self.assertEqual('test.txt', run('test.txt'))


def main():
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
    main()
