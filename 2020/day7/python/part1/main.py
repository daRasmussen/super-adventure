import re
from collections import deque

target = 'shiny gold'

db = {
    "no other bags": []
}


def hasPath(graph, src, dst):
    que = deque([src])
    while len(que) > 0:
        current = que.popleft()
        if current == dst:
            return True
        for neighbour in graph[current]:
            que.append(neighbour)
    return False


def bfs(graph, start):
    visited, queue = set(), deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print("Now visiting", node)
        visited.add(node)
        for neighbor in graph[node]:
            queue.append(neighbor)
    return visited


def create_graph(lines):
    for line in lines:
        parts = line.strip().split("contain")
        parent = parts[0]
        children = parts[1]
        key = parent.split(" bags")[:1]
        tmp = [x.strip() for x in children.split(", ")]
        tmp = [re.match("(\w+).(\w+).(\w+)", x).groups() for x in tmp]
        res = []
        for item in tmp:
            if not item[0].isnumeric():
                res.append(f"{item[0]} {item[1]} {item[2]}")
            else:
                res.append(f"{item[1]} {item[2]}")
        db[str(key[0])] = res


def main():
    with open("test.txt", "r") as data:
        create_graph(data.readlines())


if __name__ == '__main__':
    main()
    bfs(db, target)
    print(hasPath(db, target, target))
