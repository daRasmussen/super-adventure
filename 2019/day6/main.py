def get_orbits(file):
    graph = {}
    with open(file) as f:
        orbits = list(f.readlines())
        for orbit in orbits:
            node1, node2 = orbit.strip().split(")")
            graph[node2] = node1
    return graph

def count_orbits(graph, node):
    count = 0
    current = node
    while graph.get(current) is not None:
        current = graph.get(current)
        count += 1
    return count

def get_path(graph, node):
    orbits = []
    current = node
    while graph.get(current) is not None:
        current = graph.get(current)
        orbits.append(current)
    return orbits

# part 1
graph = get_orbits("data.txt")
count = 0
for node in graph.keys():
    count += count_orbits(graph, node)
print(count)
