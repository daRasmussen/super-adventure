graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}


# def depthFirstPrint(graph, source):
#    stack = [source]
#    while len(stack) > 0:
#        current = stack.pop()
#        print(current)
#        for neighbor in graph[current]:
#            stack.append(neighbor)


# def depthFirstPrint(graph, source):
#    print(source)
#    for neighbour in graph[source]:
#        depthFirstPrint(graph, neighbour)


def breadthFirstPrint(graph, source):
    que = [source]
    while len(que) > 0:
        current = que[0]
        que = que[1:]
        print(current)
        for neighbor in graph[current]:
            que.append(neighbor)


if __name__ == '__main__':
    # depthFirstPrint(graph, 'a')
    breadthFirstPrint(graph, 'a')
