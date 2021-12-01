with open('data.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]
    data = [int(x) for x in data[0]]

cups = data.copy()
current_cup = cups[0]
for _ in range(100):
    # pickup 3 cups
    x = cups.index(current_cup)
    cup1 = cups.pop((x+1)%len(cups))
    x = cups.index(current_cup)
    cup2 = cups.pop((x+1)%len(cups))
    x = cups.index(current_cup)
    cup3 = cups.pop((x+1)%len(cups))
    # find destination
    if current_cup == 1:
        destination = 9
    else:
        destination = current_cup - 1
    while destination in [cup1, cup2, cup3]:
        if destination == 1:
            destination = 9
        else:
            destination -= 1
    # insert the three cups
    x = cups.index(destination)
    if x == len(cups)-1:
        for cup in [cup1, cup2, cup3]:
            cups.append(cup)
    else:
        for cup in [cup3, cup2, cup1]:
            cups.insert(x+1, cup)
    # find next current cup
    x = cups.index(current_cup)
    x = (x+1)%len(cups)
    current_cup = cups[x]
final = ''
for num in cups:
    final += str(num)
x = final.index('1')
final = final[x+1:] + final[:x]
print(final)


