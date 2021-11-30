with open('data.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]
    fields, tickets = [], []
    
    for line in data:
        if 'or' in line:
            fields.append(line)
        elif ',' in line:
            tickets.append(line)

def get_ranges():
    ranges = {}
    for line in fields:
        line = line.split(": ")
        field = line[0]
        line = line[1].split(" or ")
        A, B = line[0].split("-"), line[1].split("-")
        lower = (int(A[0]), int(A[1]))
        upper = (int(B[0]), int(B[1]))
        ranges[field] = (lower, upper)
    return ranges


def find_invalids():
    ranges = get_ranges()
    invalid_numbers = []
    for line in tickets:
        line = line.split(',')
        ticket = [int(num) for num in line]
        for num in ticket:
            valid_number = False
            for f,r in ranges.items():
                a1, b1, a2, b2 = r[0][0], r[0][1], r[1][0], r[1][1]
                if num in range(a1,b1+1) or num in range(a2,b2+1):
                    valid_number = True
                    break
            if not valid_number:
                invalid_numbers.append(num)
    return sum(invalid_numbers)

print(find_invalids())

