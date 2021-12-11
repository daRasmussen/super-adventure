from aocd import submit, get_data

data = get_data(day=1, year=2018)
data = [int(x) for x in data.split("\n")]

ans = 0
for i in data:
    ans += i

print(ans)

submit(ans, part='a', day=1, year=2018)
# submit(ans, part='b', day=1, year=2018)
