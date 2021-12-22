from aocd import submit, get_data

data = get_data(day=19, year=2018)
ans = ''

lines = data.splitlines()
a, b = int(lines[22].split()[2]), int(lines[24].split()[2])
n = 836 + 22 * a + b

sqn = int(n ** .5)
ans = sum(d + n // d for d in range(1, sqn + 1) if n % d == 0) - sqn * (sqn ** 2 == n)
print(ans)
submit(ans, part='a', day=19, year=2018)
# submit(ans, part='b', day=19, year=2018)
