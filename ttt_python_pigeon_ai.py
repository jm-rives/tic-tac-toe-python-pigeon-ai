import random
import time

# game board
board = [[1], [2], [3],
            [4], [5], [6],
            [7], [8], [9]
            ]

game = True

num_players = int(input("Please enter the number 1 for single player or the number 2 for two players: "))

    # Check for win condition or tie
    if (turn > 8 and game == True):
        print(f"There is a TIE! Well done players! Best two out of three ; )?")
        game = False

    if turn > 3:
    # rows
        if board[0] == board[1] and board[1] == board[2]:

            print(f"Player {board[0]} is the WINNER!")
            print(display_board)
            game = False

        elif board[3] == board[4] and board[4] == board[5]:

            print(f"Player {board[3]} is the WINNER! ")
            print(display_board)
            game = False

        elif board[6] == board[7] and board[7] == board[8]:

            print(f"Player {board[0]} is the WINNER!")
            print(display_board)
            game = False
    # columns
        elif board[0] == board[3] and board[3] == board[6]:

            print(f"Player {board[0]} is the WINNER!")
            print(display_board)
            game = False

        elif board[1] == board[4] and board[4] == board[7]:

            print(f"Player {board[1]} is the WINNER!")
            print(display_board)
            game = False
        elif board[2] == board[5] and board[5] == board[8]:

            print(f"Player {board[2]} is the WINNER!")
            print(display_board)
            game = False
    # diagonal
        elif board[0] == board[4] and board[4] == board[8]:

            print(f"Player {board[0]} is the WINNER!")
            print(display_board)
            game = False

        elif board[2] == board[4] and board[4] == board[6]:

            print(f"Player {board[2]} is the WINNER!")
            print(display_board)
            game = False
        else:
            continue


