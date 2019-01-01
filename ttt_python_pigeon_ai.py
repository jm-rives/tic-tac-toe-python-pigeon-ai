import random
import time

# game board

board = [[1], [2], [3],
            [4], [5], [6],
            [7], [8], [9]
            ]

game = True
computer = True

num_players = int(input("Please enter the number 1 for single player or the number 2 for two players: \n"))

if num_players == 1:
    print("It's time for a coin toss. Player, you are 'heads'. \n")

else:
    # allow players time to choose heads or tails;
    time.sleep(2)
    computer = False
coin_toss = random.randint(0, 1) % 2


if coin_toss == 0:
    result = "Heads"
else:
    result = "Tails"

# result = 'Tails' # delete line before and uncomment above before submitting

# display winner of coin toss
if num_players == 1 and result == 'Tails':
    computer_playing_X = True
    computer_turn = True
    print(f"The {result} wins! The winner is the 💻 Computer 💻, it will play 'X' and move first\n")
else:
    computer_playing_X = False
    computer_turn = False
    print(f"The {result} wins! The winner is Player One, they will play 'X' and move first\n")

###############
# game engine #
###############

# Turn Tracker
playing_X = True # for two person play
turn = 0

while game == True:

    turn += 1
    display_board = f"{board[0]}|{board[1]}|{board[2]}\n{board[3]}|{board[4]}|{board[5]}\n{board[6]}|{board[7]}|{board[8]}\n"

#################
# Computer Play #
#################


    if computer_turn == True and computer_playing_X:
        # create an empty list to track available spots
        available_list = []
        for item in board:
            # why did I use '0' instead of i?
            if item[0] != 'X' and item[0] != 'O':
                available_list.append(item[0])
        print(available_list)
        # a computer move is selected randomly from the list of available moves
        move = random.sample(available_list, 1)
        print(move[0])

        print("The computer is playing")
        try:

            # find board coordinates
            place = board.index([(move[0])])
            board[place] = 'X'
            print(display_board)

            computer_turn = False
        except:
            print("Invalid move: Computer.")
            computer_turn = True



    else:
        print("The computer is NOT playing")
        print(display_board)
        move = int(input("Please enter the number where you want your mark:  "))
        # test to see if desired space taken
        try:
            # find board coordinates
            place = board.index([move])
            board[place] = 'O'
            computer_turn = True
        except:
            print("Sorry, that is not a valid move. Check the board and try again.")
            computer_turn = False




#####################
# Two Player Script #
#####################
    if num_players == 2:

        if  playing_X == True:
            print(display_board)
            move = int(input("Please enter the number where you want your mark:  "))

            # test to see if desired space taken
            try:
                # find board coordinates
                place = board.index([move])
                board[place] = 'X'
                playing_X = False
            except:
                print("Sorry, that is not a valid move. Check the board and try again.")
                playing_X = True

        else:
            print(display_board)
            move = int(input("Please enter the number where you want your mark:  "))
            # test to see if desired space taken
            try:
                # find board coordinates
                place = board.index([move])
                board[place] = 'O'

            except:
                print("Sorry, that is not a valid move. Check the board and try again.")
                # function call to move later in game development
                playing_X = False

            playing_X = True

#######################
# Check Tie Condition #
#######################

    if (turn > 8 and game == True):
        print(f"There is a TIE! Well done players! Best two out of three ; )?")
        game = False

###########################
# Check for Win Condition #
###########################

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


