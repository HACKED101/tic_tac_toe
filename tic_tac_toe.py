import random
import sys

moves,comp_move,user_move=0,[5],[]



def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if sign == 'O':
        print("You Win!")
    else:
        print("Computer Wins!")
    sys.exit(0)

def victory_check(board,move_list,sign):
    wind_preds=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
    c=0
    for i in wind_preds:
        for j in i:
            if j in move_list:
                c+=1
        if c == 3:
            victory_for(board,sign)
        else:
            c=0

def display_board(board,move_list,sign):
    print('+'+(7*'-'+'+')*3)
    for k in range(3):
        c=0
        for i in range(3):
            if i == 1:
                print('|',end='')
                for l in range(3):
                    if c != 2:
                        print((' ')*3+str(board[k][c])+(' ')*3+'|',end='')
                        c+=1
                    else:
                        print((' ')*3+str(board[k][c])+(' ')*3+'|')
            else:
                print('|'+(7*' '+'|')*3)
        print('+'+(7*'-'+'+')*3)
    victory_check(board,move_list,sign)
    make_list_of_free_fields(board)
    





def enter_move(board,free_sq):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    global user_move
    check=False
    while check == False:
        move=int(input('Enter your move : '))
        for i in free_sq:
            x,y=i
            if board[x][y] == move:
                user_move.append(move)
                board[x][y] = 'O'
                check=True
                break
        else:
            print('Square not free.....please try again!')
    display_board(board,user_move,'O')





def draw_move(board,free_sq):
    # The function draws the computer's move and updates the board.
    global comp_move
    check=False
    while check==False:
        move=random.randrange(1,10)
        for i in free_sq:
            x,y=i
            if board[x][y] == move:
                comp_move.append(move)
                board[x][y] = 'X'
                check=True
    display_board(board,comp_move,'X')






def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    global moves
    free_sq=[]
    for i in board:
        for j in i:
            if type(j) == int :
                free_sq.append((board.index(i),i.index(j)))
    for x in range(moves,8):
        if x%2==0:
            moves+=1
            enter_move(board,free_sq)
        else:
            moves+=1
            draw_move(board,free_sq)






board=[[1,2,3],[4,'X',6],[7,8,9]]
display_board(board,comp_move,'X')