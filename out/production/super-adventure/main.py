import re
from collections import deque

target = 'shiny gold'

db = {}


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
        for item in tmp:
            if not item[0].isnumeric():
                print(f"{item[1]} {item[2]}")
            else:
                print(f"{item[0]} {item[1]} {item[2]}")
            print(item[0], type(item[0]), item[0].isnumeric())
        # tmp = [x for x in tmp]
        # print('tmp: ', tmp)
        db[str(key[0])] = tmp


def main():
    with open("test.txt", "r") as data:
        create_graph(data.readlines())


if __name__ == '__main__':
    main()
    bfs(db, target)
