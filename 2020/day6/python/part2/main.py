import unittest


def run(path):
    with open(path, "r") as data:
        lines = data.readlines()
        groups = []
        tmp = []
        grand = []
        for line in lines:
            if line != '\n':
                tmp.append(line)
            else:
                groups.append(tmp)
                tmp = []
        for group in groups:
            voters = len(group)
            db = {}
            for person in group:
                for vote in person:
                    if vote in db:
                        db[vote] = db[vote] + person.count(vote)
                    else:
                        db[vote] = person.count(vote)
            for record in db.keys():
                grand.append(1 if db[record] == voters and record != '\n' else 0)
        return sum(grand)


class MyTestCase(unittest.TestCase):
    def test(self):
        path = 'test.txt'
        s = run(path)
        self.assertEqual(21, s)


if __name__ == '__main__':
    # unittest.main()
    # 10733 is to high
    # 3225 is to high
    # guessed 3130 is to HIGH

    # guessed 3039
    # gussed 3036

    # guessed 42
    # guessed 47
    # guessed 454
    print(run('test.txt'))
    print(run('data.txt'))
