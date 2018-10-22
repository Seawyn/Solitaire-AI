#Artur Fortunato 86388 Jorge Pacheco 86457

from search import Problem

#Tipo content

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

#Tipo pos

def make_pos(l, c):
    return (l, c)

def pos_l(pos):
    return pos[0]

def pos_c(pos):
    return pos[1]

#Tipo move

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
                    toReturn.append(make_move(make_pos(i, j), make_pos((i - 2), j)))
    return toReturn

def board_perform_move(b, move):
    b[move[0][0]][move[0][1]] = c_empty()
    b[move[1][0]][move[1][1]] = c_peg()
    if (move[0][0] == move[1][0]):
        b[ move[0][0] ][ (move[0][1] + move[1][1]) / 2 ] = c_empty()
    else:
        b[ (move[0][0] + move[1][0]) / 2 ][ move[0][1] ] = c_empty()
    return b

def areEqual(board1, board2):
    if len(board1) != board2 or len(board1[0]) != len(board2[0]):
        return False

    for i in range(len(board1)):
        line1 = board1[i]
        line2 = board2[i]

        for j in range(len(line1)):
            if line1[j] != line2[j]:
                return False
    return True

cost = float('inf')
min_path = []
current_path = []

class Solitaire(Problem):

    def __init__(self,board):
        self.board = board
        self.numberOfPegs = self.getPegs()

    def getPegs(self):
        number_of_pegs = 0

        for i in range(len(self.board)):
            line = self.board[i]
            for j in range(len(line)):
                number_of_pegs += (1 if is_peg( line[j] ) else 0)
        return number_of_pegs

    def actions(self, state):
        print(board_moves(state))

    def result(self, state, action): 
        print(board_perform_move(state, action))

    def goal_test(self, state): 
        print(self.getPegs() == 1)

    def path_cost(self, c, state1, action, state2):
        global cost
        global min_path
        global current_path

        if areEqual(state1, state2):
            cost = min(c, cost)
            min_path = current_path
        else:
            if action != []:
                state1 = board_perform_move(state1, action)
                current_path.append(action)
            actions = board_moves(state1)
            for new_action in actions:
                self.path_cost(c + 1, state1, new_action, state2)
            current_path = current_path[:-1]

    def solve(self, state1):
        if self.goal_test(state1):
            print(state1)
            return True
        moves = board_moves(state1)
        for move in moves:
            temp = board_perform_move(state1, move)
            if(self.solve(temp)):
                return True
        return False

    def h(self, node):
        print("teste")