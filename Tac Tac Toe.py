#!/usr/bin/env python
# coding: utf-8

# In[1]:


def board_positions():
    global board
    clear_output()
    board = ({'row1':['1','|','2','|','3'], 'row2':['-','-','-','-','-'],'row3':['4','|','5','|','6'],
        'row4':['-','-','-','-','-'],'row5':['7','|','8','|','9']})
    display_board(board['row1'],board['row3'],board['row5'])


# In[2]:


# Prints out the current board
from IPython.display import clear_output

def display_board(row1,row3,row5):
    
    print(''.join(board['row1']))
    print(''.join(board['row2']))
    print(''.join(board['row3']))
    print(''.join(board['row4']))
    print(''.join(board['row5']))
    pass


# In[3]:


# Initializes a new board
def new_board():
    global board
    global x_moves
    global y_moves
    
    board = ({'row1':[' ','|',' ','|',' '], 'row2':['-','-','-','-','-'],'row3':[' ','|',' ','|',' '],
          'row4':['-','-','-','-','-'],'row5':[' ','|',' ','|',' ']})
    x_moves = set()
    y_moves = set()


# In[30]:


# Takes in player whos turn it is
# Asks where they want to place their marker
# Updates board to include thier new placement
# Displays the updated board
def player_move(player):
    choice = False
    
    #runs until they have made a valid choice
    while choice == False:
        clear_output(wait = True)
        move = (input(F"{player}'s where would you like                       to place your piece? (1-9)"))
        #check if the input was a number
        if move.isnumeric() == False:
            print('Invalid entry. Please enter a number (1-9):')
        else:
            move = int(move)-1
            #check if input is in range and not yet played
            if (move) in range(0,9) and (move) not in y_moves and (move) not in x_moves:
                if player == 'X':
                    x_moves.add(move)
                    choice = True
                elif player == 'Y':
                    y_moves.add(move)
                    choice = True
            else:
                print('Invalid entry. Please enter a number (1-9):')          
          


# In[23]:


#which player's turn it is and updates the board with their move
def update_board(player):
    if player == "X":
        for move in x_moves:    
            if move in range(0,3):
                board['row1'][move*2] = player
            elif move in range(3,6):
                board['row3'][(move-3)*2] = player        
            elif move in range(6,9):
                board['row5'][(move-6)*2] = player
    else:
        for move in y_moves:    
            if move in range(0,3):
                board['row1'][move*2] = player
            elif move in range(3,6):
                board['row3'][(move-3)*2] = player        
            elif move in range(6,9):
                board['row5'][(move-6)*2] = player

    display_board(board['row1'], board['row3'], board['row5'])


# In[24]:


#checks to see if a player has won
#return True if player has won, False if not
def has_won(player):
    #win conditions:
    #all in a row
    a = {0,1,2}
    b = {3,4,5}    
    c = {6,7,8}
    #all in a column
    d = {0,3,6}
    e = {1,4,7}  
    f = {2,5,8}
    #diagonals
    g = {0,4,8}
    h = {2,4,6}
    
    if player == 'X':
        if (a.issubset(x_moves) or b.issubset(x_moves) or c.issubset(x_moves) or
           d.issubset(x_moves) or e.issubset(x_moves) or f.issubset(x_moves) or
           g.issubset(x_moves) or h.issubset(x_moves)):
            print('X Wins!')
            return True
        elif len(x_moves)==5:
            print('Tie Game!')
            return True
        else:
            return False
    elif player == 'Y':
        if (a.issubset(y_moves) or b.issubset(y_moves) or c.issubset(y_moves) or
           d.issubset(y_moves) or e.issubset(y_moves) or f.issubset(y_moves) or
           g.issubset(y_moves) or h.issubset(y_moves)):
            print('Y Wins!')
            return True
        else:
            return False
    


# In[28]:


# Initializes the game
# Starts with player X and switches back and forth between turns
# Prompts user for position choice
# Displays board for them after selected
# Checks if a player has won
# Prints f"Player {current_player} won!" when the player wins
# Asks if the player wants to play again
def game_on():
    won = False
    ready = False
    again = True
    player = 'X'
    while again == True:
        board_positions()
        while ready == False:
            check = input("These are the board positions. Are you ready? (y/n)").upper()
            if check == 'Y':
                ready = True
            elif check == 'N':
                pass
            elif check == '':
                print('Invalid entry. Are you ready? (Y/N)')
            else:
                print('Invalid entry. Are you ready? (Y/N)')
                
        new_board()

        while won == False:
            player_move(player)
            update_board(player)
            won = has_won(player)

            if player == 'X':
                player = 'Y'
            elif player == 'Y':
                player = 'X'

            if won == True:
                check = input("Would you like to play again? (y/n)").upper()
                #if yes, re-initialize variables
                if check == 'Y':
                    player = 'X'
                    won = False
                    ready = False
                    break
                else:
                    again = False
                    print("Thanks for playing!")


# In[32]:


game_on()


# In[ ]:




