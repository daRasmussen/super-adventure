from aocd import submit, get_data
from collections import namedtuple

import pytest

data = get_data(day=2, year=2018)
print("\n")
TestData = namedtuple("TestData", ["data", "result"])
TestData.__test__ = False # type: ignore

def part1(data:str) -> dict:
    res = { 2: 0, 3: 0, "checksum": 0 }
    for line in data.splitlines():
        line = line.strip()
        tmp = set()
        for c in line:
            tmp.add(c)
        dtmp = {}
        for t in tmp:
            dtmp[t] = line.count(t)
        dtmp = set(dtmp.values())
        if 2 in dtmp:
            res[2] += 1
        if 3 in dtmp:
            res[3] += 1
    res["checksum"] = res[2] * res[3]
    return res

@pytest.mark.parametrize(
    ("data", "result"),
    (
        TestData("abcdef", { 2: 0, 3: 0, "checksum": 0 }),
        TestData("bababc", { 2: 1, 3: 1, "checksum": 1 }),
        TestData("abbcde", { 2: 1, 3: 0, "checksum": 0 }),
        TestData("abcccd", { 2: 0, 3: 1, "checksum": 0 }),
        TestData("aabcdc", { 2: 1, 3: 0, "checksum": 0 }),
        TestData("abcdee", { 2: 1, 3: 0, "checksum": 0 }),
        TestData("ababab", { 2: 0, 3: 1, "checksum": 0 }),
        TestData("""
                 abcdef
                 bababc
                 abbcde
                 abcccd
                 aabcdc
                 abcdee
                 ababab
                 """, { 2: 4, 3: 3, "checksum": 12 })
    )
)
def test_part1(data, result):
    assert part1(data) == result


ans = part1(data).get("checksum")
print(ans)

# submit(ans, part='a', day=2, year=2018)

def part2(data: str) -> str:
    c2 = 0
    c3 = 0
    ids = []
    for line in data.splitlines():
        s = line.strip()
        ids.append(s)
        count = {}
        for c in s:
            if c not in count:
                count[c] = 0
            count[c] += 1
        has_two = False
        has_three = False
        for k, v in count.items():
            if v == 2:
                has_two = True
            if v == 3:
                has_three = True
        if has_two:
            c2 += 1
        if has_three:
            c3 += 1
    for x in ids:
        for y in ids:
            diff = 0
            for i in range(len(x)):
                if x[i] != y[i]:
                    diff += 1
            if diff == 1:
                ans = []
                for i in range(len(x)):
                    if x[i] == y[i]:
                        ans.append(x[i])
                return "".join(ans)


@pytest.mark.parametrize(
    ("data", "result"),
    (
        TestData("abcde\nfghij\nklmno\npqrst\nfguij\naxcye\nwvxyz\n", "fgij"),
    )
)
def test_part2(data, result):
    assert part2(data) == result

ans = part2(data)
submit(ans, part='b', day=2, year=2018)
