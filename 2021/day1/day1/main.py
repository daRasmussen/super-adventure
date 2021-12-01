with open('data.txt') as file:
    data = file.readlines()
    measurements = [int(x) for x in data]

count = 0
target = measurements[0]
for measurement in measurements:
    if measurement > target:
        count += 1
    target = measurement 
print(count)

# part 2
group_name = 0
groups = {}
group = []
while len(measurements) != 0:
    for measurement in measurements:
        if len(group) < 3:
            group.append(measurement)
        else:
            groups[group_name] = sum(group)
            group = []
            group_name += 1
            break
    measurements.pop(0)

first, second = list(groups.values()), list(groups.values())[1:]
increase = []
decrease = []
for index, value in enumerate(first):
    if index < len(second):
        if second[index] > first[index]:
            increase.append('increase')
        else:
            decrease.append('decrease')
print(len(increase))

