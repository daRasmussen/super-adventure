def get_drawn(filename: str) -> list:
    with open(filename) as f:
        return f.readline().strip().split(",")

def get_boards(filename: str) -> list:
    bs = []
    with open(filename) as f:
        li = f.readlines()
        b = []
        for i, l in enumerate(li):
            if i != 0:
                tmp = "".join(l).split(" ")
                r = [x.strip() for x in tmp if x != '']
                if len(b) < 5:
                    if len(r) > 1:
                        b.append(r)
                else:
                    bs.append(b)
                    b = []
        bs.append(b)
    return bs

filename = "data.txt"
drawn = get_drawn(filename)
boards = get_boards(filename)
player = get_boards(filename)
# clean up
for board in player:
    for row in board:
        for i, nbr in enumerate(row):
            row[i] = -1
# draw
for nbr in drawn:
    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            for z, row_nbr in enumerate(row):
                if nbr == row_nbr:
                    player[i][j][z] = nbr
                    # print(player[i][j], row)
                    prow = player[i][j]
                    if -1 not in prow:
                        # bingo row!
                        print(prow)
                    pboards = player[i]
                    v_index = 0
                    while v_index != len(row):
                        if -1 not in prow:
                            print(player[i][v_index])
                        v_index += 1

    #break

    
