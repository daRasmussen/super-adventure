from aocd import submit, get_data
import numpy as np
data = get_data(day=11, year=2018)
serial_number = int(data.strip())
rack_id = np.arange(1, 301).reshape(-1, 1) + 10
grid = rack_id * np.arange(1, 301).reshape(1, -1) # broadcasting
grid += serial_number
grid *= rack_id
grid %= 1000
grid //= 100
grid -= 5
X = np.zeros((301, 301))
# Each cell is the sum of every top left grid cell
X[1:, 1:] = grid.cumsum(axis=0).cumsum(axis=1) 
size = 3
# Each cell is the sum of the size x size square
tmp = X[size:, size:] + X[:-size, :-size] - X[size:, :-size] - X[:-size, size:] 
x, y = np.unravel_index(tmp.argmax(), tmp.shape)
ans = "{},{}".format(x+1, y+1)
print(ans)
submit(ans, part='a', day=11, year=2018)
# submit(ans, part='b', day=11, year=2018)
