#Artur Fortunato 86388 Jorge Pacheco 86457

from search import *
import copy

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
                if (j > 1 and is_peg(b[i][j - 1]) and is_empty(b[i][j - 2])):                           #Esquerda
                    toReturn.append(make_move(make_pos(i, j), make_pos(i, (j - 2))))
                if (i > 1 and is_peg(b[i - 1][j]) and is_empty(b[i - 2][j])):                           #Cima
                    toReturn.append(make_move(make_pos(i, j), make_pos((i - 2), j)))
                if (j < (len(b[i]) - 2) and is_peg(b[i][j + 1]) and is_empty(b[i][j + 2])):             #Direita
                    toReturn.append(make_move(make_pos(i, j), make_pos(i, (j + 2))))
                if (i < (len(b) - 2) and is_peg(b[i + 1][j]) and is_empty(b[i + 2][j])):                #Baixo
                    toReturn.append(make_move(make_pos(i, j), make_pos((i + 2), j)))
    return toReturn

def board_perform_move(b, move):
    novo = copy.deepcopy(b)
    novo[move[0][0]][move[0][1]] = c_empty()
    novo[move[1][0]][move[1][1]] = c_peg()
    if (move[0][0] == move[1][0]):
        novo[ move[0][0] ][round( (move[0][1] + move[1][1]) / 2 ) ] = c_empty()
    else:
        novo[round( (move[0][0] + move[1][0]) / 2 )][ move[0][1] ] = c_empty()
    return novo

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

class sol_state():
    def __init__(self, board):
        self.board = board

    def __lt__(self, other_sol_state):                          #Volatile
        return self.num_pegs(self.board) > self.num_pegs(other_sol_state.board)

    def board(self):
        return self.board

    def num_pegs(self, board):
        counter = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[i][j] == "O"):
                    counter += 1
        return counter


INFINITY = float('inf')
'''min_path = []
current_path = []'''

class solitaire(Problem):

    def __init__(self,board):
        self.board = board
        self.initial = sol_state(board)

    def getPegs(self, state):
        number_of_pegs = 0

        for i in range(len(state.board)):
            line = state.board[i]
            for j in range(len(line)):
                number_of_pegs += (1 if is_peg( line[j] ) else 0)
        return number_of_pegs

    def actions(self, state):
        return(board_moves(state.board))

    def result(self, state, action): 
        return sol_state(board_perform_move(state.board, action))

    def goal_test(self, state): 
        return(self.getPegs(state) == 1)

    def path_cost(self, c, state1, action, state2):
        '''global cost
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
            current_path = current_path[:-1] '''
        return c + 1
        
    def canFinish(self, node):
        if self.goal_test(node.state):
            return True
        moves = board_moves(node.state.board)
        for move in moves:
            node.state.board = board_perform_move(node.state.board, move)
            if(self.canFinish(node)):
                return True
        return False

    def h(self, node):
        temp = self.canFinish(copy.deepcopy(node))
        return 0 if temp else INFINITY

print([["O","O","O","X","X"],["O","O","O","O","O"],["O","_","O","_","O"],["O","O","O","O","O"]],greedy_search(solitaire([["O","O","O","X","X"],["O","O","O","O","O"],["O","_","O","_","O"],["O","O","O","O","O"]])))
