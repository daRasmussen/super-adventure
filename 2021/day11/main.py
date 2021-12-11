from aocd import submit, get_data

data = get_data(day=11, year=2021).split("\n")
print("\n")

G = []

for line in data:
    G.append([int(x) for x in line])

R = len(G)
C = len(G[0])

ans = 0
def flash(r,c):
    global ans
    ans += 1
    G[r][c] = -1
    for dr in [-1, 0, 1]:
        for dc in [-1,0,1]:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < R and 0 <= cc < C and G[rr][cc] != -1:
                G[rr][cc] += 1
                if G[rr][cc] >= 10:
                    flash(rr, cc)

for t in range(100):
    for r in range(R):
        for c in range(C):
            G[r][c] += 1
    for r in range(R):
        for c in range(C):
            if G[r][c] == 10:
                flash(r, c)
    for r in range(R):
        for c in range(C):
            if G[r][c] == -1:
                G[r][c] = 0
print(ans)
submit(ans, part='a', day=11, year=2021)
# submit(ans, part='b', day=11, year=2021)
