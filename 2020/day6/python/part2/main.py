import unittest


def parse2(tmp, number_of_votes):
    db = {}
    for item in tmp:
        c = item[0]
        if c not in db:
            db[c] = 1
        else:
            db[c] = db[c] + 1
    res = list(filter(lambda x: x == number_of_votes, db.values()))
    return sum(res)


def inc2(group):
    target = ''.join(group)
    tmp = []
    for col, person in enumerate(group):
        for row, vote in enumerate(person):
            if target.count(vote) > 1:
                tmp.append([vote, [col, row]])
    return parse2(tmp, len(group))


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
        self.assertEqual(21, s)


if __name__ == '__main__':
    unittest.main()
    # 10733 is to high
    # 3225 is to high
    # guessed 3130 is to HIGH
    # guessed 42
    # guessed 47
    # guessed 454
    # print(run('test.txt'))
    # print(run('data.txt'))
