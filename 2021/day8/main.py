from aocd import get_data, submit
from collections import defaultdict
import itertools

data = get_data(day=8, year=2021).split("\n")
ans = 0
for line in data:
    before, after = line.split("|")
    before = before.split()
    after = after.split()

    digits = {
        0: "abcefg",
        1: "cf",
        2: "acdeg",
        3: "acdfg",
        4: "bcdf",
        5: "abdfg",
        6: "abdefg",
        7: "acf",
        8: "abcdefg",
        9: "abcdfg"
    }
    for perm in itertools.permutations(list(range(8))):
        ok = True
        D = {}
        for i in range(8):
            D[chr(ord("a")+i)] = chr(ord("a")+perm[i])
        for w in before:
            w_perm = ""
            for c in w:
                w_perm += D[c]
            w_perm = "".join(sorted(w_perm))
            if w_perm not in digits.values():
                ok = False
        if ok:
            ret = ""
            print("GOT")
            for w in after:
                w_perm = ""
                for c in w:
                    w_perm += D[c]
                w_perm = "".join(sorted(w_perm))
                d = [k for k,v in digits.items() if v == w_perm]
                ret += str(d[0])
            print(ret)
            ans += int(ret)
submit(ans, part="b", day=8, year=2021)

