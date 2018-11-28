import random
import time

# game board
board = [[1], [2], [3],
            [4], [5], [6],
            [7], [8], [9]
            ]

game = True
computer = True

num_players = int(input("Please enter the number 1 for single player or the number 2 for two players: "))

if num_players == 1:
    print("It's time for a coin toss. Player, you are 'heads'. ")

else:
    # allow players time to choose heads or tails;
    time.sleep(2)
    computer = False
coin_toss = random.randint(0, 1) % 2

if coin_toss == 0:
    result = "Heads"
else:
    result = "Tails"

# display winner of coin toss
if num_players == 1 and result == 'Tails':
    print(f"The {result} wins! The winner is the 💻 Computer 💻, it will play 'X' and move first")
else:
    print(f"The {result} wins! The winner is Player One, they will play 'X' and move first")

# playing_X = True

# game engine
# turn = 0
#
# while game == True:
#     display_board = f"{board[0]}|{board[1]}|{board[2]}\n{board[3]}|{board[4]}|{board[5]} \n{board[6]}|{board[7]}|{board[8]} \n"
#
#     turn += 1
#     if  playing_X == True:
#         print(display_board)
#         move = int(input("Please enter the number where you want your mark:  "))
#
#         # test to see if desired space taken
#         try:
#             # find board coordinates
#             place = board.index([move])
#             board[place] = 'X'
#             playing_X = False
#         except:
#             print("Sorry, that is not a valid move. Check the board and try again.")
#             playing_X = True
#
#     else:
#         print(display_board)
#         move = int(input("Please enter the number where you want your mark:  "))
#         # test to see if desired space taken
#         try:
#             # find board coordinates
#             place = board.index([move])
#             board[place] = 'O'
#
#         except:
#             print("Sorry, that is not a valid move. Check the board and try again.")
#             # function call to move later in game development
#             playing_X = False
#
#         playing_X = True
#
#     # Check for win condition or tie
#     if (turn > 8 and game == True):
#         print(f"There is a TIE! Well done players! Best two out of three ; )?")
#         game = False
#
#     if turn > 3:
#     # rows
#         if board[0] == board[1] and board[1] == board[2]:
#
#             print(f"Player {board[0]} is the WINNER!")
#             print(display_board)
#             game = False
#
#         elif board[3] == board[4] and board[4] == board[5]:
#
#             print(f"Player {board[3]} is the WINNER! ")
#             print(display_board)
#             game = False
#
#         elif board[6] == board[7] and board[7] == board[8]:
#
#             print(f"Player {board[0]} is the WINNER!")
#             print(display_board)
#             game = False
#     # columns
#         elif board[0] == board[3] and board[3] == board[6]:
#
#             print(f"Player {board[0]} is the WINNER!")
#             print(display_board)
#             game = False
#
#         elif board[1] == board[4] and board[4] == board[7]:
#
#             print(f"Player {board[1]} is the WINNER!")
#             print(display_board)
#             game = False
#         elif board[2] == board[5] and board[5] == board[8]:
#
#             print(f"Player {board[2]} is the WINNER!")
#             print(display_board)
#             game = False
#     # diagonal
#         elif board[0] == board[4] and board[4] == board[8]:
#
#             print(f"Player {board[0]} is the WINNER!")
#             print(display_board)
#             game = False
#
#         elif board[2] == board[4] and board[4] == board[6]:
#
#             print(f"Player {board[2]} is the WINNER!")
#             print(display_board)
#             game = False
#         else:
#             continue


