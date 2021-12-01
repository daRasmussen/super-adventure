with open('data.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]
    
x = data.index('')
deck1 = [int(data[i]) for i in range(x) if data[i].isdigit()]
deck2 = [int(data[i]) for i in range(x+1, len(data)) if data[i].isdigit()]

# treat the decks as a queue
while len(deck1) != 0 and len(deck2) != 0:
    p1 = deck1.pop(0)
    p2 = deck2.pop(0)
    if p1 > p2:
        deck1.append(p1)
        deck1.append(p2)
    elif p2 > p1:
        deck2.append(p2)
        deck2.append(p1)
if len(deck1) == 0:
    winning_deck = deck2
else:
    winning_deck = deck1

count = 0
for i in range(len(winning_deck)):
    count += (i+1) * winning_deck[len(winning_deck) - 1 - i]
print(count)
