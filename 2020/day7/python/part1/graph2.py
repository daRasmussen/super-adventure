""" undirected graph """

"""

    edges: [
        [i,j],
        [k,i],
        [m,k],
        [k,l],
        [o,n],
    ]

"""

edges = [
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"],
]

graph = {
    'i': ['j', 'k'],
    'j': ['i'],
    'k': ['i', 'm', 'l'],
    'm': ['k'],
    'l': ['k'],
    'o': ['n'],
    'n': ['o']
}


def has_path(g, s, d, visited):
    if s == d:
        return True
    if s in visited:
        return False
    visited.add(s)

    for n in graph[s]:
        if has_path(g, n, d, visited):
            return True
    return False


def build_graph(e):
    g = {}
    for d in e:
        [a, b] = d
        if a not in g:
            g[a] = []
        if b not in g:
            g[b] = []
        g[a].append(b)
        g[b].append(a)
    return g


def undirected_path(e, a, b):
    g = build_graph(e)
    return has_path(g, a, b, set())


if __name__ == '__main__':
    r = undirected_path(edges, 'i', 'o')
    print(r)
