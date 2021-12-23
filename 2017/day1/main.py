from aocd import submit, get_data

data = get_data(day=1, year=2017)
ans = ''

def digits(digitString):
    index = 0
    final = 0
    while index < len(digitString):
        ds1 = digitString[index]
        ds2 = "-1"
        if index == len(digitString) - 1:
            ds2 = digitString[0]
        else:
            ds2 = digitString[index + 1]
        if ds1 == ds2:
            final += int(digitString[index])
        index += 1
    return final
ans = digits(data)
print(ans)
submit(ans, part='a', day=1, year=2017)
# submit(ans, part='b', day=1, year=2017)
