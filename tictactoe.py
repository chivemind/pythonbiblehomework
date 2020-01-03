#Create a board containing 9 spaces (data structure).
board = [" " for i in range(9)]

#Create a board that is a 3x3 grid.
def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
    
    print()#Empty space
    print(row1)
    print(row2)
    print(row3)
    print()#Empty space
    
#Define player turns    
def player_move(icon):
    
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
        
    print("Your turn player {}".format(icon))
    
#Ask for player input
    choice = int(input("Enter your move (1-9): ").strip())
#Check if space is available
#We need to translate choice 1-9 into cpu speak 0-8 'board[choice -1]'
#Check if space is taken, if so, ask player to choose another space.
    while board[choice-1] != " ":
        print()
        print("That space is taken!")
        choice = int(input("Pick a different number. (1-9): ").strip())
#Assign space with icon of specified player
    else:
        board[choice - 1] = icon
        
#Assign win condition
def is_victory(icon):
#Check rows, columns & diagonals
    if (board[0] == icon and board [1] == icon and board [2] == icon) or \
       (board[3] == icon and board [4] == icon and board [5] == icon) or \
       (board[6] == icon and board [7] == icon and board [8] == icon) or \
       (board[0] == icon and board [3] == icon and board [6] == icon) or \
       (board[1] == icon and board [4] == icon and board [7] == icon) or \
       (board[2] == icon and board [5] == icon and board [8] == icon) or \
       (board[0] == icon and board [4] == icon and board [8] == icon) or \
       (board[2] == icon and board [4] == icon and board [6] == icon):
       return True
    else:
        return False

#Assign "Draw/Tie" condition
def is_draw():
    if " " not in board:
        return True
    else:
        return False

#Create 'Game Loop'
while True:
#Bring board into program
    print_board()
    player_move("X")
    print_board()
#Check win condition
    if is_victory("X"):
        print("X Wins! Congrats!")
        break
#Check Draw/Tie condition
    elif is_draw():
        print("It's a draw!")
        break
    player_move("O")
    if is_victory("O"):
        print_board()
        print("O Wins! Congrats!")
        break
#Check Draw/Tie condition
    elif is_draw():
        print("It's a draw!")
        break
    