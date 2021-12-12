from aocd import submit, get_data

data = get_data(day=8, year=2018)
ns = [int(n.strip()) for n in data.split()]
i = 0

def next_int():
    global i
    global ns
    i += 1
    return ns[i-1]

def read_tree():
    nc, nm = next_int(), next_int()
    children = []
    metadata = []
    for _ in range(nc):
        children.append(read_tree())
    for _ in range(nm):
        metadata.append(next_int())
    return children, metadata

def sum_metadata(node):
    children, metadata = node
    ans = 0
    for m in metadata:
        ans += m
    for c in children:
        ans += sum_metadata(c)
    return ans

root = read_tree()
ans = sum_metadata(root)
print(ans)
# submit(ans, part='a', day=8, year=2018)

def value(node):
    children, metadata = node
    if not children:
        return sum(metadata)
    else:
        ans = 0
        for m in metadata:
            if 1 <= m <= len(children):
                ans += value(children[m-1])
        return ans

ans = value(root)
submit(ans, part='b', day=8, year=2018)
