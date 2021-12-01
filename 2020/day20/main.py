from typing import FrozenSet
from typing import NamedTuple

class Tile(NamedTuple):
    tile_id: int
    edges: FrozenSet[str]
    back_edges: FrozenSet[str]


def compute(s: str) -> int:
    tiles = []
    for tile_s in s.strip().split('\n\n'):
        lines = tile_s.splitlines()
        tileid = int(lines[0].split()[1][:-1])
        edges_f = frozenset((
            lines[1],
            ''.join(line[-1] for line in lines[1:]),
            lines[-1][::-1],
            ''.join(line[0] for line in lines[1:])[::-1],
        ))
        back_edges_f = frozenset(edge[::-1] for edge in edges_f)
        tiles.append(Tile(tileid, edges_f, back_edges_f))

    corners = []
    for i, tile in enumerate(tiles):
        edges = set(tile.edges)
        for j, other in enumerate(tiles):
            if i == j:
                continue
            for edge in tuple(edges):
                if edge in other.edges | other.back_edges:
                    edges.discard(edge)
        if len(edges) == 2:
            corners.append(tile.tile_id)

    n = 1
    for corner in corners:
        n *= corner
    return n

with open('data.txt') as file:
    print(compute(file.read()))
