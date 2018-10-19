class agente:
    def c_peg():
        return "O"

    def c_empty():
        return "_"

    def c_blocked():
        return "X"

    def is_empty(e):
        return e == c_empty()

    def is_peg(e):
        return e == c_peg()

    def is_blocked(e):
        return e == c_blocked()

    def make_pos(l, c):
        return (l, c)

    def pos_l(pos):
        return pos[0]

    def pos_c(pos):
        return pos[1]

    def make_move(i, f):
        return[i, f]

    def move_initial(move):
        return move[0]

    def move_final(move):
        return move[1]

def board_moves(b):
    toReturn = []
    for i in range(len(b)):
        for j in range(len(b[i])):
            if not (is_peg(b[i][j])):              #If it's empty, proceed to next iteration
                continue
            else:
                if (j < (len(b[i]) - 2) and is_peg(b[i][j + 1]) and is_empty(b[i][j + 2])):
                    toReturn.append(make_move(make_pos(i, j), make_pos(i, (j + 2))))
                if (i < (len(b) - 2) and is_peg(b[i + 1][j]) and is_empty(b[i + 2][j])):
                    toReturn.append(make_move(make_pos(i, j), make_pos((i + 2), j)))
                if (j > 1 and is_peg(b[i][j - 1]) and is_empty(b[i][j - 2])):
                    toReturn.append(make_move(make_pos(i, j), make_pos(i, (j - 2))))
                if (i > 1 and is_peg(b[i - 1][j]) and is_empty(b[i - 2][j])):
                    toReturn.append(make.move(make_pos(i, j), make_pos((i - 2), j)))
    return toReturn

def board_perform_move(b, move):
    b1[move[0][0]][move[0][1]] = c_empty()
    b1[move[1][0]][move[1][1]] = c_peg()
    if (move[0][0] == move[1][0]):
        if (pos_c(move_initial(move)) > pos_c(move_final(move))):
            b[pos_l(move_final(move))][pos_l(move_final(move)) + 1] = c_empty()
        else:
            b[pos_l(move_initial(move))][pos_c(move_initial(move)) + 1] = c_empty()
    else:
        if (pos_l(move_initial(move)) > pos_l(move_final(move))):
            b[pos_l(move_final(move)) + 1][pos_c(move_final(move))] = c_empty()
        else:
            b[pos_l(move_initial(move)) + 1][pos_c(move_initial(move))] = c_empty()

b1 = [["_", "O", "O", "O", "_"], ["O", "_", "O", "_", "O"], ["_", "O", "_", "O", "_"], ["O", "_", "O", "_", "_"], ["_", "O", "_", "_", "_"]]
def main():
    print(board_moves(b1))

main()
