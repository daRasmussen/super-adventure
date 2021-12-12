from aocd import submit, get_data
import numpy as np
import itertools
import matplotlib.pyplot as plt
#from matplotlib_terminal import plt
from numpy.lib.arraysetops import unique

data = get_data(day=6, year=2018)
coords = []
for line in data.splitlines():
    x, y = line.split(",")
    coords.append((x, y))
x_coords = [int(x) for x, _ in coords]
y_coords = [int(y) for _, y in coords]
coords = list(zip(x_coords, y_coords))

def get_shortest_distance(point):
    distances = [abs(point[0] - coord[0]) + abs(point[1] - coord[1]) for coord in coords]
    distances = np.array(distances)
    if sorted(distances)[0] == sorted(distances)[1]:
        return -1 
    return distances.argmin() + 1

largest_coord = max(x_coords+y_coords)
# Create permuations of all coordinates
perm = itertools.product(list(range(largest_coord)), repeat=2)
# Store closest coordinate (or -1 if tied)
distances = [get_shortest_distance(x) for x in perm]

grid = np.array(distances).reshape(largest_coord, largest_coord)

plt.figure(figsize=(12,8))
plt.title('Visualisation of areas')
plt.scatter(x_coords, y_coords, color='r', label='Coordinates')
plt.legend()
plt.imshow(grid.T)
plt.axis('off')

edges = [grid[0], grid[max(x_coords)-1], grid[:,0], grid[:, max(y_coords)-1]]
np.unique(edges)

unique, count = np.unique(grid, return_counts=True)
inner_areas = [x for x in sorted(zip(count, unique)) if x[1] not in np.unique(edges)]
ans, _ = inner_areas[-1]
print(ans)
# submit(ans, part='a', day=6, year=2018)

def is_point_under_total_distance(point, distance=10000):
    distances = [abs(point[0] - coord[0]) + abs(point[1] - coord[1]) for coord in coords]
    if sum(distances) < 10000:
        return 1
    return 0
p = itertools.product(list(range(max(x_coords+y_coords))), repeat=2)
under_10k = [is_point_under_total_distance(x) for x in p]
ans = (sum(under_10k))
print(ans)
submit(ans, part='b', day=6, year=2018)
