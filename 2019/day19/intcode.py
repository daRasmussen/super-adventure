from aocd import get_data

data = get_data(day=5, year=2019)

OP = [int(x) for x in data.split(",")]

P = [x for x in OP]
ip = 0
while True:
    print(ip)
    digits = [int(x) for x in str(P[ip])]
    opcode = (0 if len(digits) == 1 else digits[-2]) * 10 + digits[-1]
    digits = digits[:-2]
    if opcode == 1:
        while len(digits) < 3: 
            digits = [0] + digits
        i1, i2, i3, = P[ip+1], P[ip+2], P[ip+3]
        print(opcode,i1,i2,i3,digits)
        P[i3] = (i1 if digits[2] == 1 else P[i1]) + (i2 if digits[1] == 1 else P[i2])
        ip += 4
    elif opcode == 2:
        while len(digits) < 3:
            digits = [0] + digits
        i1, i2, i3 = P[ip+1], P[ip+2], P[ip+3]
        print(opcode,i1,i2,i3,digits)
        P[i3] = (i1 if digits[2] == 1 else P[i1]) * (i2 if digits[1] == 1 else P[i2])
        ip += 4
    elif opcode == 3:
        i1 = P[ip+1]
        P[i1] = 5 # special input 
        ip += 2
    elif opcode == 4:
        i1 = P[ip+1]
        print(P[i1])
        ip += 2
    elif opcode == 5:
        while len(digits) < 2:
            digits = [0] + digits
        i1, i2 = P[ip+1], P[ip+2]
        if (i1 if digits[1]==1 else P[i1]) != 0:
            ip = (i2 if digits[0] == 1 else P[i2])
        else:
            ip += 3
    elif opcode == 6:
        while len(digits) < 2:
            digits = [0] + digits
        i1, i2 = P[ip+1], P[ip+2]
        if (i1 if digits[1] == 1 else P[i1]) == 0:
            ip = (i2 if digits[0] == 1 else P[i2])
        else:
            ip += 3
    elif opcode == 7:
        while len(digits) < 3:
            digits = [0]+digits
        i1, i2, i3 = P[ip+1], P[ip+2], P[ip+3]
        if (i1 if digits[2] == 1 else P[i1]) < (i2 if digits[1] == 1 else P[i2]):
            P[i3] = 1
        else:
            P[i3] = 0
        ip += 4
    elif opcode == 8:
        while len(digits) < 3:
            digits = [0]+digits
        i1, i2, i3 = P[ip+1], P[ip+2], P[ip+3]
        if (i1 if digits[2] == 1 else P[i1]) == (i2 if digits[1] == 1 else P[i2]):
            P[i3] = 1
        else:
            P[i3] = 0
        ip += 4
    else: 
        assert opcode == 99
        break
