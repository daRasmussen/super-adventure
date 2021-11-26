import re
from collections import deque

target = 'shiny gold'

rules = {}

def find():
    total = 0
    for rule in rules:
        bags = [rule]
        while len(bags) > 0:
            if bags[0] in rules:
                for newbag in rules[bags[0]]:
                    if newbag[1] not in bags:
                        bags.append(newbag[1])
            del bags[0]
            if target in bags:
                total += 1
                break
    print(total)

def create_graph(lines):
    for line in lines:
        parts = line.strip().split("contain")
        parent = parts[0]
        children = parts[1]
        key = parent.split(" bags")[:1]
        tmp = [x.strip() for x in children.split(", ")]
        tmp = [re.match("(\w+).(\w+).(\w+)", x).groups() for x in tmp]
        tmp = [[int(x[0])  if x[0].isnumeric() else 0, f"{x[1]} {x[2]}" ] for x in tmp]
        rules[str(key[0])] = tmp


def main():
    with open("data.txt", "r") as data:
        create_graph(data.readlines())


if __name__ == '__main__':
    main()
    find()
