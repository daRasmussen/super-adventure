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
    with open("test.txt", "r") as data:
        lines = data.readlines()
        random.shuffle(lines)
        target = "shiny gold"
        rules = {}
        """ Create rules. """
        for line in lines:
            parent, child = line.strip().split("bags contain")
            rules[parent.strip()] = [child]

        c = 1
        cc = []
        """ Search """
        while target != 'no other bags.':
            for rule in rules:
                if rule == target:
                    child = rules[rule][0]
                    target = get_parent(child)
                    count = get_count(child)
                    if count != 0:
                        c = c * count
                        cc.append(c)
                        print(target, child, c, cc, sum(cc))



               
