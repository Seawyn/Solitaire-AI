#Artur Fortunato 86388 Jorge Pacheco 86457

from search import *
import copy
#import os
#import psutil
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

class sol_state():
    def __init__(self, board):
        self.board = board

    def __lt__(self, other_sol_state):                          #Volatile
        return len(board_moves(self.board)) > len(board_moves(other_sol_state.board))

    def num_pegs(self, board):
        counter = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (board[i][j] == "O"):
                    counter += 1
        return counter

class solitaire(Problem):

    def __init__(self,board):
        self.initial = sol_state(board)
        Problem(self, self.initial)
        self.number_of_x = self.getBlockeds(self.initial)

    def getPegs(self, state):
        number_of_pegs = 0

        for i in range(len(state.board)):
            line = state.board[i]
            for j in range(len(line)):
                number_of_pegs += (1 if is_peg( line[j] ) else 0)
        return number_of_pegs

    def getBlockeds(self, state):
        number_of_x = 0
        for l in state.board:
            number_of_x += l.count(c_blocked())
        return number_of_x
    
    def actions(self, state):
        return(board_moves(state.board))

    def result(self, state, action): 
        return sol_state(board_perform_move(state.board, action))

    def goal_test(self, state): 
        return self.getPegs(state) == 1

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def h(self, node):
        return self.getPegs(node.state) * self.getBlockeds(node.state)

