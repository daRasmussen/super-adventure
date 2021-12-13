from aocd import submit, get_data
from collections import defaultdict

data = get_data(day=9, year=2018)

ppp = data.split(";")[0].split(" ")[0]
poo = data.split(";")[1].split(" ")[-2]

num_players = int(ppp)
num_marbles = int(poo) * 100

marbles = [0]
current = 0
score = defaultdict(int)
for m in range(1, num_marbles):
   if m % 23 == 0:
       score[m%num_players] += m
       current = (current - 7 + len(marbles))%len(marbles)
       score[m%num_players] += marbles[current]
       marbles = marbles[:current] + marbles[current+1:]
   else:
       current = (current+2)%len(marbles)
       marbles = marbles[:current] + [m] + marbles[current:]
ans = max(score.values())
print(ans)

submit(ans, part='b', day=9, year=2018)
