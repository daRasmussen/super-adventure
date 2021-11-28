with open('data.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]

def get_acc(): 
    acc = 0
    line = 0
    instructions = [] 

    current_instruction = data[line]
    while line not in instructions: 
        instructions.append(line)
        
        current_instruction = data[line]
        current_instruction = current_instruction.split()
        cmd = current_instruction[0]
        num = int(current_instruction[1])

        if cmd == 'acc':
            acc += num
            line += 1
        elif cmd == 'jmp':
            line += num
        elif cmd == 'nop':
            line += 1
    return acc

acc = get_acc()
print(acc)

# part 2 
def get_acc_eof():
    acc = 0
    line = 0
    instructions = [] 

    current_instruction = data[line]
    while line not in instructions: 
        instructions.append(line)
        
        current_instruction = data[line]
        current_instruction = current_instruction.split()
        cmd = current_instruction[0]
        num = int(current_instruction[1])

        if cmd == 'acc':
            acc += num
            line += 1
        elif cmd == 'jmp':
            line += num
        elif cmd == 'nop':
            line += 1

        if line >= len(data):
            return acc, True

    return acc, False

for i in range(len(data)):
    if 'jmp' in data[i]:
        data[i] = data[i].replace('jmp', 'nop')
        acc, found = get_acc_eof()
        if found:
            print(acc)
            break
        else:
            data[i] = data[i].replace('nop', 'jmp')
