from aocd import submit, get_data
from collections import defaultdict, deque

data = get_data(day=9, year=2018)

max_players = data.split(";")[0].split(" ")[0]
last_marble =data.split(";")[1].split(" ")[-2]

def play_game(max_players, last_marble):
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 1000 == 0:
            print(marble)
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0

ans = play_game(int(max_players), int(last_marble)*100)
print(ans)
print(max_players, last_marble*100)
submit(ans, part='b', day=9, year=2018)
