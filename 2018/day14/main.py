from aocd import submit, get_data

data = get_data(day=14, year=2018)
ans = ''
data = data.strip()
score = '37'
elf1 = 0
elf2 = 1
while data not in score[-7:]:
    score += str(int(score[elf1]) + int(score[elf2]))
    elf1 = (elf1 + int(score[elf1]) + 1) % len(score)
    elf2 = (elf2 + int(score[elf2]) + 1) % len(score)
ans = score[int(data):int(data)+10]
print(ans)
submit(ans, part='a', day=14, year=2018)
# submit(ans, part='b', day=14, year=2018)
