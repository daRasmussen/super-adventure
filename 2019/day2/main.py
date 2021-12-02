with open('data.txt') as f:
    d = f.readlines()
    d = [x.strip() for x in d]
    li = d[0].split(",")
    li = [int(x) for x in li]
    li[1] = 12
    li[2] = 2
t= []
for l in li:
    if len(t) != 4:
        t.append(l)
        if len(t) == 4:
            i, a, b, o = t[0], t[1], t[2], t[3]
            if i == 1:
                li[o] = li[a] + li[b]
            if i == 2:
                li[o] = li[a] * li[b]
            if i == 99:
                break
    else:
        t = [l]
print(li[0])

# part 2
with open('data.txt') as f:
    d = f.readlines()
    d = [x.strip() for x in d]
    li = d[0].split(",")
    li = [int(x) for x in li]
noun, verb = [0, 1]
li[1] = noun
li[2] = verb
t = 19690720
p = [] 
while li[0] != t:
    noun, verb = li[0], li[1]
    if noun == verb:
        noun += 1
    elif noun > verb:
        verb += 1
    elif noun < verb:
        noun += 1
    for a in li:
        if len(p) != 4:
            p.append(a)
            if len(p) == 4:
                c, a, b, o = p[0], p[1], p[2], p[3]
                print('li:',len(li),'c: ', c,'a: ',a,'b: ', 'o: ', o)
                if c == 1:
                    li[o] = li[a] + li[b]
                if c == 2:
                    li[o] = li[a] * li[b]
                if c == 99:
                    break
        else:
            p = [a]
    print(100 * li[0] + li[1])
