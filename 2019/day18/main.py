import sys
from aocd import submit, get_data
from collections import deque, namedtuple

data = get_data(day=18, year=2019)
print("\n")
G = []
for line in data.split("\n"):
    G.append(list(line))
R = len(G)
C = len(G[0])
DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]
Q = deque()
State = namedtuple("State", ["pos", "keys", "d"])
all_keys = {}
starts = []
for r in range(R):
    for c in range(C):
        if G[r][c] == "@":
            starts.append((r,c))
        if 'a'<=G[r][c]<='z':
            all_keys[G[r][c]] = (r,c)
print(len(all_keys), all_keys)
Q.append(State(starts,set(),0))
N = len(starts)

best = 1e9
SEEN = {}
while Q:
    S = Q.popleft()
    key = (tuple(S.pos), tuple(sorted(S.keys)))
    if key in SEEN and S.d>=SEEN[key]:
        continue
    SEEN[key] = S.d
    if len(SEEN)%10000 == 0:
        print(key, S.d)
        print(len(SEEN))
    newkeys = set(S.keys)
    bad = False
    for i in range(N):
        r,c = S.pos[i]
        if not (0<=r<R and 0<=c<C and G[r][c]!="#"):
            bad = True
            break
        if 'A'<=G[r][c]<='Z' and G[r][c].lower() not in S.keys:
            bad = True
            break
    if bad:
        continue


    D = {}
    Q2 = deque()
    for i in range(N):
        Q2.append((S.pos[i], i, 0))
    while Q2:
        pos,robot,dd = Q2.popleft()
        r,c = pos
        if not (0<=r<R and 0<=c<C and G[r][c]!="#"):
            continue
        if 'A'<=G[r][c]<='Z' and G[r][c].lower() not in S.keys:
            continue
        if pos in D:
            continue
        D[pos] = (dd,robot)
        for d3 in range(4):
            newpos = (r+DR[d3], c+DC[d3])
            Q2.append((newpos, robot, dd+1))
    for k in all_keys:
        if k not in S.keys and all_keys[k] in D:
            distance,robot = D[all_keys[k]]
            newpos = list(S.pos)
            newpos[robot] = all_keys[k]
            newkeys = set(S.keys)
            newkeys.add(k)
            newdist = S.d+distance
            if len(newkeys) == len(all_keys):
                if newdist < best:
                    best = newdist 
                    print(best)
            Q.append(State(newpos, newkeys, newdist))

#submit(best, part="b", day=18, year=2019)
