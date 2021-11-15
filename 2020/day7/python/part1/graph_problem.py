graph_problem = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": []
}


def hasPath(graph, src, dst):
    que = [src]
    while len(que) > 0:
        current = que.pop(0)
        if current == dst:
            return True
        for neighbour in graph[current]:
            que.append(neighbour)
    return False


# def hasPath(graph, src, dst):
#    Depth First Recursive
#    if src == dst:
#        return True
#    for neighbour in graph[src]:
#        if hasPath(graph, neighbour, dst):
#            return True
#    return False


if __name__ == '__main__':
    res0 = hasPath(graph_problem, 'f', 'k')
    print(res0)
    res1 = hasPath(graph_problem, 'f', 'ö')
    print(res1)
