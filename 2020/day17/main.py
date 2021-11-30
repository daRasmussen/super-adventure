with open('data.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]

def get_initial_active_points(four_dimensions):
    active_points = set()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '#':
                if not four_dimensions:
                    active_points.add((i, j, 0))
                else:
                    active_points.add((i, j, 0, 0))
    return active_points

# part 1
active_points = get_initial_active_points(False)
for r in range(6):
    new_active_points = set()
    # check each x, y, z point
    for x in range(-10-r,r+10):
        for y in range(-10-r,r+10):
            for z in range(-2-r,r+2):
                # for the current x,y,z check the neighbors
                active_count = 0
                for i in range(-1,2):
                    for j in range(-1,2):
                        for k in range(-1,2):
                            if not (i == 0 and k == 0 and j == 0):
                                if (x+i, y+j, z+k) in active_points:
                                    active_count += 1
                # apply rules
                if (x,y,z) in active_points and (active_count == 2 or active_count == 3):
                    new_active_points.add((x,y,z))
                if (x,y,z) not in active_points and active_count == 3:
                    new_active_points.add((x,y,z))
    active_points = new_active_points

print(len(active_points))

# part 2
active_points = get_initial_active_points(True)
for r in range(6):
    new_active_points = set()
    # check each x, y, z, w point
    for x in range(-10-r,r+10):
        for y in range(-10-r,r+10):
            for z in range(-2-r,r+2):
                for w in range(-2-r,r+2):

                    # for the current x,y,z,w check the neighbors
                    active_count = 0
                    for i in range(-1,2):
                        for j in range(-1,2):
                            for k in range(-1,2):
                                for p in range(-1,2):
                                    if not (i == 0 and k == 0 and j == 0 and p == 0):
                                        if (x+i, y+j, z+k, w+p) in active_points:
                                            active_count += 1
                    # apply rules
                    if (x,y,z,w) in active_points and (active_count == 2 or active_count == 3):
                        new_active_points.add((x,y,z,w))
                    if (x,y,z,w) not in active_points and active_count == 3:
                        new_active_points.add((x,y,z,w))
    active_points = new_active_points
    print(len(active_points))
print(len(active_points))

