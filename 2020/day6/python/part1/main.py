import unittest

unique = ['a', 'b', 'c']


def inc(g, s):
    tmp = []
    for i in g:
        line = list(i)
        for c in line:
            if tmp.count(c) == 0:
                tmp.append(c)
                s = s + 1
    return s


def run(path):
    s = 0
    g = []
    t = []
    with open(path, "r") as data:
        for line in data:
            l = line.strip()
            if '' != l:
                t.append(l)
            else:
                g.append(t)
                t = []
        if len(t) != 0:
            g.append(t)
        for p in g:
            s = inc(p, s)
    return s


# F9 breakpoint
class MyTestCase(unittest.TestCase):
    def test(self):
        path = 'test.txt'
        s = run(path)
        self.assertEqual(11, s)


if __name__ == '__main__':
    unittest.main()
    # print(run('data.txt'))
