from aocd import submit, get_data

data = get_data(day=1, year=2017)
ans = ''

def compute(s: str) -> int:
    s = s.strip()
    total = 0
    half = len(s) // 2
    for i, c in enumerate(s):
        if s[(i + half) % len(s)] == c:
            total += int(c)
    return total

ans = compute(data)
print(ans)
submit(ans, part='b', day=1, year=2017)
