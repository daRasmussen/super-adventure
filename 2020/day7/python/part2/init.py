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
        cc = []
        """ Search """
        while target != 'no other bags.':
            for rule in rules:
                if rule == target:
                    for child in rules[rule]:
                        target = get_parent(child)
                        count = get_count(child)
                        if count != 0:
                            c = c * count
                            cc.append(c)
                            print(target, child, c, cc, sum(cc))



               
