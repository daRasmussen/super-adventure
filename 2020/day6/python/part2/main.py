import unittest


def parse2(tmp, ref):
    s = sum(range(1, ref))
    db = {}
    for item in tmp:
        c = item[0]
        c_n = c + '_col'
        col = item[1][0]
        db[c_n] = sum(range(1, col + 1), 0)
    res = list(filter(lambda x: x == s, db.values()))
    return res[0] // s if res else 0


def inc2(group):
    if len(group) == 1:
        return len(group[0])
    else:
        target = ''.join(group)
        tmp = []
        for col, person in enumerate(group):
            for row, vote in enumerate(person):
                if target.count(vote) > 1:
                    tmp.append([vote, [col, row]])
        return parse2(tmp, len(group)) if tmp else 0


def run(path):
    s = 0
    g = []
    t = []
    with open(path, "r") as data:
        for line in data:
            li = line.strip()
            if '' != li:
                t.append(li)
            else:
                g.append(t)
                t = []
        if len(t) != 0:
            g.append(t)
        for p in g:
            s = s + inc2(p)
    return s


# F9 breakpoint
class MyTestCase(unittest.TestCase):
    def test(self):
        path = 'test.txt'
        s = run(path)
        self.assertEqual(6, s)


if __name__ == '__main__':
    # unittest.main()
    # guessed 3130 is to HIGH
    # guessed 42
    # guessed 47
    # guessed 454
    print(run('test.txt'))
    print(run('data.txt'))
