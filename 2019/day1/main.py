with open('data.txt') as file:
    data = file.readlines()
    masses = [int(x) for x in data]
total = []
for mass in masses:
    total.append(mass // 3 - 2)
    
print(sum(total))

# part 2
total = []
for mass in masses:
    target = mass // 3 - 2
    if target // 3 - 2 < 0:
        total.append(mass // 3 - 2)
    else:
        total.append(target)
        while target > 0:
            target = target // 3 - 2
            if target > 0:
                total.append(target)
print(sum(total))
