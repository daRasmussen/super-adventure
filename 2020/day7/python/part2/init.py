import re
import math


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
        target = "shiny gold"
        rules = {}
        """ Create rules. """
        for index, line in enumerate(lines):
            parent, child = line.strip().split("bags contain")
            rules[parent.strip()] = [child]

        c = 0 # TODO: ADD COUNT !
        """ Search """
        while target != 'no other bags.':
            for rule in rules:
                if rule == target:
                    child = rules[rule][0]
                    target = get_parent(child)
                    print(target, child)
                    #print(target != 'other bags.')
                #print(target)



               
