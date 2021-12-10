from itertools import *
from math import gcd
from aocd import submit, get_data

data = get_data(day=22, year=2019)

shuffles = [x.strip().split() for x in data.split("\n")]

N = 10007
new_stack_i = lambda i: N-i-1
cut_i = lambda i, n:  (i-n)%N
deal_i = lambda i, n: (i*n)%N

def track_pos(i):
    for shuf in shuffles:
        if shuf[0]=="cut":
            i = cut_i(i, int(shuf[1]))
        elif shuf[0]=="deal" and shuf[2]=="increment":
            i = deal_i(i, int(shuf[-1]))
        elif shuf[0]=="deal" and shuf[-1]=="stack":
            i = new_stack_i(i)
    return i
ans = track_pos(2019)
submit(ans, part='a', day=22, year=2019)

# submit(ans, part='b', day=22, year=2019)
