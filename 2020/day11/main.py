with open('data.txt') as file: 
    data = file.readlines()
    data = [list(line.strip()) for line in data]
    original = data.copy()

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

def get_adjacent_count2(row, col):
    count = 0
    # i is for row, j for col
    i_U, i_D, j_R, j_L = row-1, row+1, col+1, col-1
    N, S, E, W, NE, SE, NW, SW = False, False, False, False, False, False, False, False

    while not (N and S and W and E and NE and NW and SW):
        # Check North
        if not N and i_U >= 0:
            if data[i_U][col] == '#':
                count += 1
                N = True
            elif data[i_U][col] == 'L':
                N = True
        else:
            N = True
        # Check South 
        if not S and i_D <= len(data)-1:
            if data[i_D][col] == '#':
                count += 1
                S = True
            elif data[i_D][col] == 'L':
                S = True
        else:
            S = True
        # Check East
        if not E and j_R <= len(data[row])-1:
            if data[row][j_R] == '#':
                count += 1
                E = True
            elif data[row][j_R] == 'L':
                E = True
        else:
            E = True
        # Check West
        if not W and j_L >= 0:
            if data[row][j_L] == '#':
                count += 1
                W = True
            elif data[row][j_L] == 'L':
                W = True
        else:
            W = True
        # Check North West
        if not NW and i_U >= 0 and j_L >= 0:
            if data[i_U][j_L] == '#':
                count += 1
                NW = True
            elif data[i_U][j_L] == 'L':
                NW = True
        else:
            NW = True
        # Check South West
        if not SW and i_D <= len(data)-1 and j_L >= 0:
            if data[i_D][j_L] == '#':
                count += 1
                SW = True
            elif data[i_D][j_L] == 'L':
                SW = True
        else:
            SW = True
        # Check North East
        if not NE and i_U >= 0 and j_R <= len(data[row])-1:
            if data[i_U][j_R] == '#':
                count += 1
                NE = True
            elif data[i_U][j_R] == 'L':
                NE = True
        else:
            NE = True
        # Check South East
        if not SE and i_D <= len(data)-1 and j_R <= len(data[row])-1:
            if data[i_D][j_R] == '#':
                count += 1
                SE = True
            elif data[i_D][j_R] == 'L':
                SE = True
        else: 
            SE = True
       
        i_U -= 1
        i_D += 1
        j_R += 1
        j_L -= 1
    return count

def run_rules(tolerance):
    new_seating = []
    for row in range(len(data)):
        current_row = data[row]
        new_row = []
        for col in range(len(current_row)):
            if current_row[col] == '.':
                new_row.append('.')
                continue
            adjacent_count = 0
            if tolerance == 4:
                adjacent_count = get_adjacent_count(row, col)
            elif tolerance == 5:
                adjacent_count = get_adjacent_count2(row, col)
            if current_row[col] == 'L' and adjacent_count == 0:
                new_row.append('#')
            elif current_row[col] == '#' and adjacent_count >= tolerance:
                new_row.append('L')
            else:
                new_row.append(current_row[col])
        new_seating.append(new_row)
    for i in range(len(data)):
        data[i] = new_seating[i]

def get_final_count(tolerance):
    prev = data.copy()
    run_rules(tolerance)
    while data != prev:
        prev = data.copy()
        run_rules(tolerance)

    return get_num_occupied()

print(get_final_count(4))

# part 2
data = original.copy()
print(get_final_count(5))
