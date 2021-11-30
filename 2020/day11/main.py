with open('data.txt') as file: 
    data = file.readlines()
    data = [list(line.strip()) for line in data]

def get_num_occupied():
    count = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '#':
                count += 1
    return count

def get_adjacent_count(row, col):
    count = 0
    current_row = data[row]
    # check left
    if col-1 >= 0:
        if current_row[col-1] == '#':
            count += 1
    # check right
    if col+1 <= len(current_row)-1:
        if current_row[col+1] == '#':
            count += 1
    # check above
    if row-1 >= 0:
        above_row = data[row-1] 
        if above_row[col] == '#':
            count += 1
        if col-1 >= 0:
            if above_row[col-1] == '#':
                count += 1
        if col+1 <= len(above_row)-1:
            if above_row[col+1] == '#':
                count += 1
    # check below
    if row+1 <= len(data)-1:
        below_row = data[row+1] 
        if below_row[col] == '#':
            count += 1
        if col-1 >= 0:
            if below_row[col-1] == '#':
                count += 1
        if col+1 <= len(below_row)-1:
            if below_row[col+1] == '#':
                count += 1
    return count

def run_rules():
    new_seating = []
    for row in range(len(data)):
        current_row = data[row]
        new_row = []
        for col in range(len(current_row)):
            if current_row[col] == '.':
                new_row.append('.')
                continue
            adjacent_count = get_adjacent_count(row, col)
            if current_row[col] == 'L' and adjacent_count == 0:
                new_row.append('#')
            elif current_row[col] == '#' and adjacent_count >= 4:
                new_row.append('L')
            else:
                new_row.append(current_row[col])
        new_seating.append(new_row)
    for i in range(len(data)):
        data[i] = new_seating[i]

def get_final_count():
    prev = data.copy()
    run_rules()
    while data != prev:
        prev = data.copy()
        run_rules()

    return get_num_occupied()

print(get_final_count())
