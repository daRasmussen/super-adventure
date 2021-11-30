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
    valid_tickets = [] 

    for line in tickets:
        line = line.split(',')
        ticket = [int(num) for num in line]
        valid_ticket = True
        for num in ticket:
            valid_number = False
            for f,r in ranges.items():
                a1, b1, a2, b2 = r[0][0], r[0][1], r[1][0], r[1][1]
                if num in range(a1,b1+1) or num in range(a2,b2+1):
                    valid_number = True
                    break
            if not valid_number:
                invalid_numbers.append(num)
                valid_ticket = False
        if valid_ticket:
            valid_tickets.append(ticket)

    return sum(invalid_numbers), valid_tickets

num, valid_tickets = find_invalids()
print(num)

def solve_fields():
    ranges = get_ranges()
    valid_columns = {}
    for field, r in ranges.items():
        valid_columns[field] = []
        a1, b1, a2, b2 = r[0][0], r[0][1], r[1][0], r[1][1]
        for i in range(len(valid_tickets[0])):
            found = True
            for ticket in valid_tickets:
                num = ticket[i]
                if not (num in range(a1,b1+1) or num in range(a2,b2+1)):
                    found = False
                    break
            if found:
                valid_columns[field].append(i)
    solved_indicies = []
    solved_fields = {}
    for i in range(len(fields)):
        for field, possible_columns in valid_columns.items():
            if len(possible_columns) == i+1:
                for j in possible_columns:
                    if j not in solved_indicies:
                        solved_indicies.append(j)
                        solved_fields[field] = j
                        break
    total = 1
    for field, col in solved_fields.items():
        if 'departure' in field:
            total *= valid_tickets[0][col]
    return total

print(solve_fields())

