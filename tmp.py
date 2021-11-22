import json
import random


def get_vertex():
    x = random.randint(0, 1)
    y = random.randint(0, 1)
    z = random.randint(0, 1)
    return [x, y, z]


def create_vertices():
    vertices = []
    for i in range(0, 9):
        while len(vertices) != i:
            v = get_vertex()
            if v not in vertices:
                vertices.append(v)
            else:
                v = get_vertex()
    return vertices


def create_edges(vertices):
    edges = []
    for index in range(0, 4):
        edge = []
        for vertex in vertices:
            edge.append(vertex)
        edges.append(edge)
    return edges


if __name__ == '__main__':
    vertices = create_vertices()
    edges = create_edges(vertices)
    res = {
        "type": "Solid",
        "coordinates": [
            vertices
        ],
        "vertices": [
            vertices
        ],
        "origin": [0, 0, 0]
    }
    print(json.dumps(res))
