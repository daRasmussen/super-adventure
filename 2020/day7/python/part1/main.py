import unittest

import getopt
import sys

target = 'shiny gold'

test_graph = {
    'Amin': {'Wasim', 'Nick', 'Mike'},
    'Wasim': {'Imran', 'Amin'},
    'Imran': {'Wasim', 'Faras'},
    'Faras': {'Imran'},
    'Mike': {'Amin'},
    'Nick': {'Amin'}
}

my_graph = {
    'light red': {'bright white', 'muted yellow'},
    'dark orange': {'bright white', 'muted yellow'},
    'bright white': {'shiny gold'},
    'muted yellow': {'shiny gold', 'faded blue'},
    'shiny gold': {'bright white', 'muted yellow'},
    'dark olive': {'faded blue', 'dotted black'},
    'vibrant plum': {'faded blue', 'dotted black'},
    'faded blue': {'vibrant plum', 'dark olive'},
    'dotted black': {'dark olive'}
}


def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited


def run(path):
    print('RUN', path)
    print(bfs(test_graph, 'Amin'))
    print(bfs(my_graph, 'bright white'))
    print(bfs(my_graph, 'muted yellow'))
    db = {}
    with open(path, "r") as data:
        lines = data.readlines()


# 19, 6, 9, 26, 14, 49, 576


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
