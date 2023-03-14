# initialize the board
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# define function to print the board
def print_board():
    print("   |   |   ")
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")
    print("   |   |   ")

# define function to check if someone has won
def check_win(player):
    if board[0] == board[1] == board[2] == player:
        return True
    elif board[3] == board[4] == board[5] == player:
        return True
    elif board[6] == board[7] == board[8] == player:
        return True
    elif board[0] == board[3] == board[6] == player:
        return True
    elif board[1] == board[4] == board[7] == player:
        return True
    elif board[2] == board[5] == board[8] == player:
        return True
    elif board[0] == board[4] == board[8] == player:
        return True
    elif board[2] == board[4] == board[6] == player:
        return True
    else:
        return False

# define function to play the game
def play_game():
    # set the starting player to X
    current_player = "X"
    # set the game_over flag to False
    game_over = False

    # loop while the game is not over
    while not game_over:
        # print the current board
        print_board()

        # get the current player's move
        move = int(input(f"{current_player}'s turn. Enter a position (1-9): "))

        # check if the move is valid
        if board[move-1] != " ":
            print("That position is already taken. Try again.")
            continue

        # update the board with the current player's move
        board[move-1] = current_player

        # check if the current player has won
        if check_win(current_player):
            print_board()
            print(f"{current_player} wins!")
            game_over = True
            break

        # check if the board is full (i.e. a tie)
        if " " not in board:
            print_board()
            print("It's a tie!")
            game_over = True
            break

        # switch the current player to the other player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

# play the game
play_game()
