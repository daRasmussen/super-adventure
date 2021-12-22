from aocd import submit, get_data
from typing import List, Tuple

data = get_data(day=21, year=2021)
ans = None

def load_data() -> List[int]:
    p1 = data.splitlines()[0].split(":")[1]
    p2 = data.splitlines()[1].split(":")[1]
    return [int(p1),int(p2)]
 
 
def calculate_cycles(p1_start: int, p2_start: int) -> Tuple[List[int], List[int]]:
    cycle_length = 10
    cycle_range = range(cycle_length)
    p1_moves, p2_moves = \
        [[((((6 * (i + 1) - j) * 3) - 1) % 10) + 1 for i in cycle_range] for j in (4, 1)]
    p1_cycle, p2_cycle = [[i] * cycle_length for i in (p1_start, p2_start)]
    for i in cycle_range:
        p1_cycle[i] = ((p1_moves[i] - 1 + p1_cycle[i - 1]) % 10) + 1
        p2_cycle[i] = ((p2_moves[i] - 1 + p2_cycle[i - 1]) % 10) + 1
    return p1_cycle, p2_cycle
 
 
def find_winning_turn(target: int, cycle: List[int]) -> int:
    full_cycles = int(target / sum(cycle))
    points = full_cycles * sum(cycle)
    i = 0
    while points < target:
        points += cycle[i]
        i += 1
    return (full_cycles * len(cycle)) + i
 
 
def find_score_at_turn(turn: int, cycle: List[int]):
    full_cycles = int(turn / len(cycle))
    points = full_cycles * sum(cycle)
    i = 0
    while (full_cycles * len(cycle)) + i < turn:
        points += cycle[i]
        i += 1
    return points
 
 
def simulate_deterministic(p1_start: int, p2_start: int, target: int = 1000) -> int:
    p1_cycle, p2_cycle = calculate_cycles(p1_start, p2_start)
    p1_winning_turn = find_winning_turn(target, p1_cycle)
    p2_winning_turn = find_winning_turn(target, p2_cycle)
    if p1_winning_turn <= p2_winning_turn:
        losing_score = find_score_at_turn(p1_winning_turn - 1, p2_cycle)
        total_rolls = (6 * p1_winning_turn) - 3
    else:
        losing_score = find_score_at_turn(p2_winning_turn, p1_cycle)
        total_rolls = 6 * p2_winning_turn
    return losing_score * total_rolls
 
p1_start, p2_start = load_data()
ans = simulate_deterministic(p1_start, p2_start)
print(ans)
submit(ans, part='a', day=21, year=2021)
# submit(ans, part='b', day=21, year=2021)
