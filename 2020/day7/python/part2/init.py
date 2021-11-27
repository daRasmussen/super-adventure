import re
import math
import random

def get_count(child):
    if child == ' no other bags.':
        return 0
    return int(re.findall(r"\d+", child)[0])

def get_parent(child):
    if child == ' no other bags.':
        return 'no other bags.'
    x = child.split(" ")
    return f"{x[2]} {x[3]}"


if __name__ == '__main__':
    with open("data.txt", "r") as data:
        lines = data.read().splitlines()
        random.shuffle(lines)
        target = "shiny gold"
        rules = {}
        """ Create rules. """
        for line in lines:
            parent, children = line.strip().split("bags contain")
            rules[parent.strip()] = children.split(",")
        c = 1
        levels = {}
        index = 1
        """ Search """
        while target != 'no other bags.':
            for rule in rules:
                if rule == target:
                    children = rules[rule]
                    tmp = []
                    for child in children:
                        target = get_parent(child)
                        count = get_count(child)
                        tmp.append(count)
                    levels[index] = tmp
                    index += 1
        cc = []
        for level in levels:
            b = sum(levels[level])
            cc.append(b**level)
        print(cc, sum(cc))
"""
                1 gold
    1 red      2 black       3 yellow 
1 2 3         4 5 6         7 8 9

1 * 6      + 2 (4 + 5 + 6) + 3 (7 + 8 + 9) 
"""









