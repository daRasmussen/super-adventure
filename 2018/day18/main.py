from aocd import submit, get_data

data = get_data(day=18, year=2018)
ans = ''

from collections import defaultdict, Counter

OPEN, TREE, LUMBER = ('.', '|', '#')

def get_next_generation(lines):
    next_lines = []
    num_rows, num_cols = len(lines), len(lines[0])

    for r in range(num_rows):
        new_row = []

        for c in range(num_cols):
            counts = defaultdict(int)

            for delta_c in range(-1, 2):
                for delta_r in range(-1, 2):
                    if delta_r == delta_c == 0:
                        continue

                    r_adj, c_adj = r + delta_r, c + delta_c

                    if 0 <= r_adj < num_rows and 0 <= c_adj < num_cols:
                        counts[lines[r_adj][c_adj]] += 1

            if lines[r][c] == OPEN and counts[TREE] >= 3:
                new_row.append(TREE)

            elif lines[r][c] == TREE and counts[LUMBER] >= 3:
                new_row.append(LUMBER)

            elif lines[r][c] == LUMBER and counts[LUMBER] >= 1 and counts[TREE] >= 1:
                new_row.append(LUMBER)

            elif lines[r][c] == LUMBER:
                new_row.append(OPEN)

            else:
                new_row.append(lines[r][c])

        next_lines.append(new_row)

    return next_lines


def get_resource_value(lines, num_minutes):
    layouts_seen = {}
    resource_values = {}
    cycle_start = cycle_end = 0

    for cur_minute in range(1, num_minutes + 1):
        lines = get_next_generation(lines)
        key = ''.join(''.join(line) for line in lines)
        counts = Counter(key)
        resource_values[cur_minute] = counts[TREE] * counts[LUMBER]

        if key in layouts_seen:
            cycle_start = layouts_seen[key]
            cycle_end = cur_minute
            break

        layouts_seen[key] = cur_minute

    period = cycle_end - cycle_start
    cycle_containing = num_minutes - cycle_start

    if period and cycle_containing:
        num_minutes = cycle_start + cycle_containing % period

    return resource_values[num_minutes]


lines = [list(map(str, line.strip())) for line in data.splitlines()]
ans = get_resource_value(lines, 10)
print(ans)
submit(ans, part='a', day=18, year=2018)
# submit(ans, part='b', day=18, year=2018)
