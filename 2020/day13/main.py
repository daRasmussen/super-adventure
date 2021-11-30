with open('data.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]
    data[1] = data[1].split(',')

def get_id_minutes():
    arrival = int(data[0])
    ids = data[1]
    lowest = 9999999999999999999
    low_id = 0
    for item in ids:
        if item != 'x':
            id = int(item)
        else:
            continue
        id_multiple = arrival // id
        difference = (id * (id_multiple + 1)) - arrival
        if difference < lowest:
            lowest = difference
            low_id = id
    return low_id * lowest

print(get_id_minutes())

