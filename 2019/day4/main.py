def has_repeated_adjacent(num):
    number = str(num)
    last = number[0]
    for digit in number[1:]:
        if digit == last:
            return True
        else:
            last = digit
    return False

def has_a_double_adjacent(num):
    number = str(num)
    last = number[0]
    group = 1
    for digit in number[1:]:
        if digit == last:
            group += 1
        else:
            if group == 2:
                return True
            last = digit
            group = 1
    return group == 2

def is_non_decreasing(num):
    number = str(num)
    last = number[0]
    for digit in number[1:]:
        if digit < last:
            return False
        last = digit
    return True

# part 1 
with open("data.txt") as f:
    d = f.read().strip().split("-")
    d = [ int(x) for x in d]

start, end = d[0], d[1]
r = len([num for num in range(start, end + 1) if has_repeated_adjacent(num) and is_non_decreasing(num)])
print(r)

# part 2
r = len([num for num in range(start, end + 1) if has_a_double_adjacent(num) and is_non_decreasing(num)])
print(r)
