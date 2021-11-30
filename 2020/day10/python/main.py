with open('data.txt') as file:
    data = file.readlines()
    data = [ int(line.strip()) for line in data ]
    data.sort()
data = [0] + data
data.append(max(data)+3)

def get_differences_count():
    count1 = 0
    count3 = 0 

    for i in range(len(data)-1):
        diff = data[i+1] - data[i]
        if diff == 1:
            count1 += 1
        elif diff == 3:
            count3 += 1
    return count1 * count3

print(get_differences_count())

# part 2
checked = {}
def get_num_ways(pos):
    if pos == len(data) - 1:
        return 1
    if pos in checked:
        return checked[pos]
    total = 0
    for i in range(pos+1, len(data)):
        if data[i] - data[pos] <= 3:
            total += get_num_ways(i)
    checked[pos] = total
    return total

print(get_num_ways(0))
