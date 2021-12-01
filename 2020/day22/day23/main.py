with open('data.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]
    data = [int(x) for x in data[0]]

cups = data.copy()
current_cup = cups[0]
for _ in range(100):
    # pickup 3 cups
    x = cups.index(current_cup)
    cup1 = cups.pop((x+1)%len(cups))
    x = cups.index(current_cup)
    cup2 = cups.pop((x+1)%len(cups))
    x = cups.index(current_cup)
    cup3 = cups.pop((x+1)%len(cups))
    # find destination
    if current_cup == 1:
        destination = 9
    else:
        destination = current_cup - 1
    while destination in [cup1, cup2, cup3]:
        if destination == 1:
            destination = 9
        else:
            destination -= 1
    # insert the three cups
    x = cups.index(destination)
    if x == len(cups)-1:
        for cup in [cup1, cup2, cup3]:
            cups.append(cup)
    else:
        for cup in [cup3, cup2, cup1]:
            cups.insert(x+1, cup)
    # find next current cup
    x = cups.index(current_cup)
    x = (x+1)%len(cups)
    current_cup = cups[x]
final = ''
for num in cups:
    final += str(num)
x = final.index('1')
final = final[x+1:] + final[:x]
print(final)

# part 2
class Node:
    def __init__(self, val, prev=None, n=None):
        self.val = val
        self.prev = prev
        self.next = n
class CircularLinkedList:
    def __init__(self):
        self.nodes = {}

    def insert_left(self, val, prev_node=None) -> Node:
        new_node = Node(val)
        if prev_node is None:
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.prev = prev_node
            new_node.next = prev_node.next
            new_node.prev.next = new_node
            new_node.next.prev = new_node
        self.nodes[val] = new_node
        return new_node
    def pop_right(self, left_node=None) -> int:
        pop_node = left_node.next
        pop_val = pop_node.val
        left_node.next = pop_node.next
        pop_node.next.prev = left_node
        del pop_node
        del self.nodes[pop_val]
        return pop_val
    def find(self, val) -> Node:
        return self.nodes[val]
    def get_list(self, marker=1):
        nums = []
        marker_node = self.nodes[marker]
        nums.append(marker_node.val)
        marker_node = marker_node.next
        while marker_node.val != marker:
            nums.append(marker_node.val)
            marker_node = marker_node.next
        return nums
cups = CircularLinkedList()
prev_node = None
for x in data:
    prev_node = cups.insert_left(x, prev_node)
   
for x in range(max(data)+1, 1000001):
    prev_node = cups.insert_left(x, prev_node)

current_cup = cups.find(data[0])
for i in range(10000000):
    if i%10000 == 0:
        print(i)
    # pick up 3 cups
    cup1 = cups.pop_right(current_cup)
    cup2 = cups.pop_right(current_cup)
    cup3 = cups.pop_right(current_cup)
    # find destination
    if current_cup.val == 1:
        x = 1000000
    else:
        x = current_cup.val - 1

    while x in [cup1, cup2, cup3]:
        if x == 1:
            x = 1000000
        else:
            x -= 1
    # insert the cups
    destination_cup = cups.find(x)
    for cup in [cup3, cup2, cup1]:
        cups.insert_left(cup, destination_cup)

    del destination_cup

    # update current cup
    current_cup = current_cup.next

cup1 = cups.find(1)
total = cup1.next.val * cup1.next.next.val
print(total)
