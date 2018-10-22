#H = Número de pegs - 1

class sol_state():
    def __init__(self, board):
        self.board = board
        
    def __lt__(self, other_sol_state):                          #Volatile
        return self.board < other_sol_state

    def board():
        return self.board

    def num_pegs():
        counter = 0
        for i in range(len(board)):
            for j in range(len(len(board[i]))):
                if (board[i][j] == "O"):
                    counter += 1
        return counter

class solitaire(Problem):
    def __init__(self, board):
        self.board = board

    def actions(self, state):
        return board_moves(state)

    def result(self, state, action):
        board_perform_move(state, action)

    def goal_test(self, state):
        Cstate = sol_state(state)
        return Cstate.num_pegs() == 1

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def h(self, node):
        raise NotImplementedError

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
                if (j > 1 and is_peg(b[i][j - 1]) and is_empty(b[i][j - 2])):                           #Esquerda
                    toReturn.append(make_move(make_pos(i, j), make_pos(i, (j - 2))))
                if (i > 1 and is_peg(b[i - 1][j]) and is_empty(b[i - 2][j])):                           #Cima
                    toReturn.append(make.move(make_pos(i, j), make_pos((i - 2), j)))
                if (j < (len(b[i]) - 2) and is_peg(b[i][j + 1]) and is_empty(b[i][j + 2])):             #Direita
                    toReturn.append(make_move(make_pos(i, j), make_pos(i, (j + 2))))
                if (i < (len(b) - 2) and is_peg(b[i + 1][j]) and is_empty(b[i + 2][j])):                #Baixo
                    toReturn.append(make_move(make_pos(i, j), make_pos((i + 2), j)))
    return toReturn

def board_perform_move(b, move):
    b[move[0][0]][move[0][1]] = c_empty()
    b[move[1][0]][move[1][1]] = c_peg()
    print("Comparing ", move[0], " and ", move[1])
    if (move[0][0] == move[1][0]):
        b[pos_l(move_final(move))][round((pos_c(move_final(move)) + pos_c(move_initial(move))) / 2)] = c_empty()
    else:
        b[round((pos_c(move_final(move)) + pos_c(move_initial(move))) / 2)][pos_l(move_final(move))] = c_empty()
    print(b1)