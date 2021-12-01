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

# part 2

def rec_combat(deck1, deck2):
    """ Return 'p1' or 'p2', depending on who wings. """
    previous_rounds = []
    while len(deck1) != 0 and len(deck2) != 0:
        if (deck1, deck2) in previous_rounds:
            return 'p1'
        else:
            previous_rounds.append((deck1.copy(), deck2.copy()))
            p1 = deck1.pop(0)
            p2 = deck2.pop(0)
            # deterime winner with a sub game 
            if len(deck1) >= p1 and len(deck2) >= p2:
                winner = rec_combat(deck1.copy()[:p1], deck2.copy()[:p2])
                if winner == 'p1':
                    deck1.append(p1)
                    deck1.append(p2)
                else:
                    deck2.append(p2)
                    deck2.append(p1)
            # determine winner by card value
            else:
                if p1 > p2:
                    deck1.append(p1)
                    deck1.append(p2)
                elif p2 > p1:
                    deck2.append(p2)
                    deck2.append(p1)
    if len(deck1) == 0:
        return 'p2'
    else:
        return 'p1'

deck1 = [int(data[i]) for i in range(x) if data[i].isdigit()]
deck2 = [int(data[i]) for i in range(x+1, len(data)) if data[i].isdigit()]

winner = rec_combat(deck1, deck2)
if winner == 'p1':
    winning_deck = deck1
else:
    winning_deck = deck2

count = 0
for i in range(len(winning_deck)):
    count += (i+1) * winning_deck[len(winning_deck) - 1 - i]
print(count)


