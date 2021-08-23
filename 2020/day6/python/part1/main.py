import unittest

unique = ['a', 'b', 'c']


def run(path):
    s = 0
    g = []
    t = []
    with open(path, "r") as data:
        for line in data:
            l = line.strip()
            if l != '':
                t.append(l)
            else:
                g.append(t)
                t = []
        if len(t) != 0:
            g.append(t)
        has_a = False
        has_b = False
        has_c = False
        for p in g:
            if len(p) == 1:
                if p[0].find('a') and has_a is False:
                    s = s + 1
                    has_a = True
                if p[0].find('b') and has_b is False:
                    s = s + 1
                    has_b = True
                if p[0].find('c') and has_c is False:
                    s = s + 1
                    has_c = True
                    
    return s


# F9 breakpoint
class MyTestCase(unittest.TestCase):
    def test(self):
        path = 'test.txt'
        s = run(path)
        self.assertEqual(11, s)


if __name__ == '__main__':
    unittest.main()
