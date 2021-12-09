from aocd import submit, get_data

data = get_data(day=9, year=2021)
G = [[int(x) for x in line.strip()] for line in data.split("\n")]

R = len(G)
C = len(G[0])
DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]
ans = 0
for r in range(R):
    for c in range(C):
        ok = True
        for d in range(4):
            rr = r+DR[d]
            cc = c+DC[d]
            if 0<=rr<R and 0<=cc<C and G[rr][cc]<=G[r][c]:
                ok = False
        if ok:
            ans += G[r][c] + 1
             
submit(ans, part='a', day=9, year=2021)
# submit(ans, part='b', day=9, year=2021)
