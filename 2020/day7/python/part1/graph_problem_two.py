from collections import deque

graph_test = {
    0: [1, 4],
    1: [0, 2, 3, 4],
    2: [1, 3],
    3: [1, 2, 4],
    4: [0, 1, 3]
}


def dfs(graph, start):
    """ Depth First Search """
    visited, stack = set(), [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            # perform some operations on the node
            # for example, we print out the node
            print("Now visiting", node)
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
    return visited


def bfs(graph, start):
    """ Breadth-First Search """
    visited, queue = set(), deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            # perform some operations on the node
            print("Now visiting", node)
        visited.add(node)
        for neighbor in graph[node]:
            queue.append(neighbor)
    return visited


def dfs_path(graph, src, dst):
    stack = [(src, [src])]
    visited = set()
    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        if node == dst:
            return path
        visited.add(node)
        for neighbor in graph[node]:
            stack.append((neighbor, path + [neighbor]))
    return None


def bfs_path(graph, src, dst):
    """ EQ weight == Djiankstras shortest path algorithm. """
    visited, queue = set(), deque([[src]])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node in visited:
            continue
        if node == dst:
            return path
        for neighbor in graph[node]:
            queue.append(path + [neighbor])
    return None


if __name__ == '__main__':
    # dfs(graph_test, 0)
    # bfs(graph_test, 0)
    print(dfs_path(graph_test, 0, 2))
    print(bfs_path(graph_test, 0, 2))
