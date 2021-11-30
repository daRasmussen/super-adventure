with open('data.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]
    data[1] = data[1].split(',')

def get_id_minutes():
    arrival = int(data[0])
    ids = data[1]
    lowest = 9999999999999999999
    low_id = 0
    for item in ids:
        if item != 'x':
            id = int(item)
        else:
            continue
        id_multiple = arrival // id
        difference = (id * (id_multiple + 1)) - arrival
        if difference < lowest:
            lowest = difference
            low_id = id
    return low_id * lowest

print(get_id_minutes())

# part 2 
# Chinese remainder theorem 
# bus k at index i departs at a time t+1
# t+i % k == 0
# t % k == -i
# t % k == k-i
# index = (k - (i%k)) % k

def mod_inverse(a, n):
    # find some x such that (a*x) % n == 1
    a = a % n
    if n == 1:
        return 1
    for x in range(1, n):
        if ((a * x) % n == 1):
            return x

def get_earliest_time():
    ids = []
    full_product = 1
    for i in range(len(data[1])):
        item = data[1][i]
        if item != 'x':
            k = int(item)
            i = i % k
            ids.append(((k-i)%k,k))
            full_product *= k
    total = 0
    for i,k in ids:
        partial_product = full_product // k
        inverse = mod_inverse(partial_product,k)
        assert (inverse * partial_product) % k == 1
        term = inverse * partial_product * i
        total += term
    return total % full_product

print(get_earliest_time())
