#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output
def TicTacToe(board):
    clear_output()
    print(board[7]+'    $  '+board[8]+'  $  '+board[9])
    print('----------------')
    print(board[4]+'    $  '+board[5]+'  $  '+board[6])
    print('----------------')
    print(board[1]+'    $  '+board[2]+'  $  '+board[3])
    
    
entries=['']*10
TicTacToe(entries)


def players_entry():
    choice=""
    while(choice!='o' and choice!='x'):
        choice=input('Player1, please enter your choice  ')
    player1=choice
    if(player1=='x'):
        player2='o'
    else:
        player2='x'
    return (player1,player2)


def choose_place(board,symbol,place):
    board[place]=symbol
    

def winner(board,symbol):
    return(board[1]==symbol and board[2]==symbol and board[3]==symbol) or (board[4]==symbol and board[5]==symbol and board[6]==symbol) or (board[7]==symbol and board[8]==symbol and board[9]==symbol) or (board[1]==symbol and board[4]==symbol and board[7]==symbol) or (board[2]==symbol and board[5]==symbol and board[8]==symbol) or (board[3]==symbol and board[6]==symbol and board[9]==symbol) or (board[1]==symbol and board[5]==symbol and board[9]==symbol) or (board[3]==symbol and board[5]==symbol and board[7]==symbol)


import random
def DecideFirstPlayer():
    FirstPlayer=random.randint(0,1)
    if(FirstPlayer==0):
        return "PLAYER1"
    else:
        return "PLAYER2"
    

def PlaceAvailable(board,place):
    return(board[place]==' ')


def BoardFull(board):
    for i in range(1,10):
        if(PlaceAvailable(board,i)):
            return False
    return True


def NextMove(board):
    place=0
    while(place not in [1,2,3,4,5,6,7,8,9] and not PlaceAvailable(board,place)):
        place=int(input("Next Move please: "))
    return place


def replay():
    desire=input("Want to play again?")
    return(desire =="y")


print("WELCOME TO TIC TAC TOE")
while(True):
    gameboard=[' ']*10
    player1,player2=players_entry()
    turn=DecideFirstPlayer()
    print(turn+'will play first')
    start=input('Are you ready? y or n?')
    if start=='y':
        game_start= True
    else:
        game_start= False
    while(game_start):
        if(turn=='PLAYER1'):
            TicTacToe(gameboard)
            place=NextMove(gameboard)
            choose_place(gameboard,player1,place)
            if(winner(gameboard,player1)):
                TicTacToe(gameboard)
                print("Winner is Player1")
                game_start=False
            else:
                if(BoardFull(gameboard)):
                    TicTacToe(gameboard)
                    print("TIE!!")
                    break
                else:
                    turn='PLAYER2'
        else:
            TicTacToe(gameboard)
            place=NextMove(gameboard)
            choose_place(gameboard,player2,place)
            if(winner(gameboard,player2)):
                TicTacToe(gameboard)
                print("Winner is Player2")
                game_start=False
            else:
                if(BoardFull(gameboard)):
                    TicTacToe(gameboard)
                    print("TIE!!")
                    game_start=False
                else:
                    turn='PLAYER1'
    if not replay():
        break


# In[ ]:




