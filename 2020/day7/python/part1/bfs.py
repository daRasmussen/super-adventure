g = {
    'Amin': {'Wasim', 'Nick', 'Mike'},
    'Wasim': {'Imran', 'Amin'},
    'Imran': {'Wasim', 'Faras'},
    'Faras': {'Imran'},
    'Mike': {'Amin'},
    'Nick': {'Amin'}
}


def bfs2(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop()
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited


if __name__ == '__main__':
    print(bfs2(g, 'Amin'))
