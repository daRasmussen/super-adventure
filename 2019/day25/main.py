from aocd import submit, get_data

data = get_data(day=25, year=2019).split(",")
OP  = [int(x) for x in data]
print("\n")

ans = ''
# submit(ans, part='a', day=25, year=2019)
# submit(ans, part='b', day=25, year=2019)

from collections import defaultdict, deque
import sys

class Program(object):
    def __init__(self, pid, data, input):
        self.P = defaultdict(int)
        for i, x in enumerate(data):
            self.P[i] = int(x)
        self.input = input
        self.ip = 0
        self.pid = pid
        self.rel_base = 0
        self.halted = False
    def idx(self, i, I):
        mode = (0 if i >= len(I) else I[i])
        val = self.P[self.ip+1+i]
        if mode == 0:
            pass # no - op
        elif mode == 2:
            val = val + self.rel_base
        else:
            assert False, mode
        return val
    def val(self, i, I):
        mode = (0 if i >= len(I) else I[i])
        val = self.P[self.ip+1+i]
        if mode == 0:
            val = self.P[val]
        elif mode == 2:
            val = self.P[val+self.rel_base]
            print('val: ', val, "rel_base: ", self.rel_base)
        return val
    def run_all(self):
        ans = []
        while True:
            val = self.run()
            if val == None:
                return ans
            ans.append(val)
    def run(self):
        """ Return next output  """
        while True:
            cmd = str(self.P[self.ip])
            opcode = int(cmd[-2:])
            I = list(reversed([int(x) for x in cmd[:-2]]))
            # print(opcode, I, self.P[self.ip:self.ip+4])
            if opcode == 1:
                # i1, i2 = self.val(0, I), self.val(1, I)
                #while len(self.P) <= self.idx(2, I):
                #    self.P.append(0)
                self.P[self.idx(2, I)] = self.val(0, I) + self.val(1, I)
                self.ip += 4
            elif opcode == 2:
                # i1, i2 = self.val(0,I), self.val(1, I)
                #while len(self.P) <= self.idx(2, I):
                #    self.P.append(0)
                self.P[self.idx(2, I)] = self.val(0, I) * self.val(1, I)
                self.ip += 4 
            elif opcode == 3:
                #while len(self.P) <= self.idx(0, I):
                #    self.P.append(0)
                self.P[self.idx(0, I)] = self.input
                #self.Q.pop(0)
                self.ip += 2
            elif opcode == 4:
                ans = self.val(0, I)
                self.ip += 2
                return ans
            elif opcode == 5:
                self.ip = self.val(1, I) if self.val(0, I) != 0 else self.ip + 3
            elif opcode == 6:
                self.ip = self.val(1, I) if self.val(0, I) == 0 else self.ip + 3
            elif opcode == 7:
                #while len(self.P) <= self.idx(2, I):
                #    self.P.append(0)
                print('TEEEST: :::::: ', self.val(0, I))
                self.P[self.idx(2, I)] = (1 if self.val(0,I) < self.val(1, I) else 0)
                self.ip += 4
            elif opcode == 8:
                #while len(self.P) <= self.idx(2, I):
                #    self.P.append(0)
                self.P[self.idx(2, I)] = (1 if self.val(0, I) == self.val(1, I) else 0)
                self.ip += 4
            elif opcode == 9:
                self.rel_base += self.val(0, I)
                self.ip += 2
            else:
                assert opcode == 99, opcode
                self.halted = True
                return None


Q = deque()
def get_input():
    if Q:
        return Q.popleft()
    cmd = input()
    for c in cmd:
        Q.append(ord(c))
    Q.append(ord("\n"))
    return get_input()

P = Program("0", data, get_input)
while not P.halted:
    o = int(P.run() or 0)
    if P.halted:
        break
    if o <= 255:
        sys.stdout.write(chr(o))
    else:
        sys.stdout.write(str(o))



#CMDS = [
#        "south",
#        "take cake",
#        "south",
#        "west",
#        "take mutex",
#        "east",
#        "north",
#        "north",
#        "west",
#        "take klien bottle",
#        "south",
#        "east",
#        "take monolith",
#        "south",
#        "take fuel cell",
#        "west",
#        "west",
#        "take astrolabe",
#        "east",
#        "east",
#        "north",
#        "west",
#        "north",
#        "west",
#        "north",
#        "take tambourine",
#        "south",
#        "west",
#        "take dark matter",
#        "west"
#]
#items = [
#    "mutex",
#    "dark matter",
#    "klein bottle",
#    "tambourine",
#    "fuel cell",
#    "astrolabe",
#    "monolith",
#    "cake",
#]
#for item in items:
#    CMDS.append(f"drop {item}")
#for a in range(2**len(items)):
#    iset = set()
#    for i in range(len(items)):
#        if ((a>>i)%1) == 1:
#            iset.add(items[i])
#    print(a, iset)
#    for item in iset:
#        CMDS.append(f"take {item}")
#    CMDS.append("north")
#    for item in iset:
#        CMDS.append(f"drop {item}")
#
#cmds = []
#Q = deque()
#def get_input():
#    if Q:
#        return Q.popleft()
#    if CMDS:
#        cmd = CMDS.pop(0)
#    else:
#        cmd = input()
#    if cmd == "QUIT":
#        print(cmds)
#        sys.exit(0)
#    cmds.append(cmd)
#    for c in cmd:
#        Q.append(ord(c))
#    Q.append(ord("\n"))
#    return get_input()
#
#P = Program("0", OP, get_input)
#while not P.halted:
#    o = int(P.run() or 0)
#    if P.halted:
#        break
#    if o <= 255:
#        sys.stdout.write(chr(o))
