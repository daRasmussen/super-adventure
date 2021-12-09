from aocd import get_data
import itertools

data = get_data(day=9, year=2019)

class Program(object):
    def __init__(self, pid, data, inputs):
        self.P = [int(x) for x in data.split(",")]
        self.Q = inputs
        self.ip = 0
        self.pid = pid
        self.rel_base = 0 
    def idx(self, i):
        return self.P[self.ip+1+i]
    def val(self, i, I):
        mode = (0 if i >= len(I) else I[i])
        val = self.P[self.ip+1+i]
        if mode == 0:
            val = self.P[val]
        elif mode == 2:
            val = self.P[val+self.rel_base]
        return val
    def run(self):
        """ Return next output  """
        while True:
            cmd = str(self.P[self.ip])
            opcode = int(cmd[-2:])
            I = list(reversed([int(x) for x in cmd[:-2]]))
            print(opcode,I,self.P[self.ip:self.ip+4])
            if opcode == 1:
                while len(self.P) <= self.idx(2):
                    self.P.append(0)
                self.P[self.idx(2)] = self.val(0, I) + self.val(1, I)
                self.ip += 4
            if opcode == 2:
                while len(self.P) <= self.idx(2):
                    self.P.append(0)
                self.P[self.idx(2)] = self.val(0, I) * self.val(1, I)
                self.ip += 4
            elif opcode == 3:
                while len(self.P) <= self.idx(0):
                    self.P.append(0)
                self.P[self.idx(0)] == self.Q[0]
                self.Q.pop(0)
                self.ip += 2
            elif opcode == 4:
                ans = self.val(0, I)
                self.ip += 2
                return ans
            elif opcode == 5:
                self.ip = self.val(1, I) if self.val(0, I) != 0 else self.ip +3
            elif opcode == 6:
                self.ip = self.val(1, I) if self.val(0, I) == 0 else self.ip +3
            elif opcode == 7:
                while len(self.P) <= self.idx(2):
                    self.P.append(0)
                self.P[self.idx(2)] = (1 if self.val(0, I) < self.val(1,I) else 0) 
                self.ip += 4
            elif opcode == 8:
                self.P[self.idx(2)] = (1 if self.val(0,I) == self.val(1, I) else 0)
            elif opcode == 9:
                self.rel_base += self.val(0, I)
                self.ip += 2
            else:
                assert opcode == 99, opcode
                return None

PERM = itertools.permutations([5,6,7,8,9])
ans = 0
for perm in PERM:
    THREAD = [Program(i, data, [perm[i]]) for i in range(len(perm))]
    THREAD[0].Q.append(0)
    score = 0
    done = False
    while not done:
        for i in range(len(perm)):
            val = THREAD[i].run()
            print("RET", i, val, THREAD[i].Q, THREAD[i].ip)
            if val == None:
                print(perm, score)
                if score > ans:
                    ans = score
                done = True
                break
            elif i == len(perm) - 1:
                score = val
            THREAD[(i+1)%len(THREAD)].Q.append(val)
print(ans)
