# Tic-Tac-Toe Game (2 Players)

# Create the game board
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]


# Function to display the board
def display_board():

    print()

    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")

    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")

    print(" " + board[6] + " | " + board[7] + " | " + board[8])

    print()


# Function to check winner
def check_winner(player):

    # Check rows
    if board[0] == player and board[1] == player and board[2] == player:
        return True

    elif board[3] == player and board[4] == player and board[5] == player:
        return True

    elif board[6] == player and board[7] == player and board[8] == player:
        return True

    # Check columns
    elif board[0] == player and board[3] == player and board[6] == player:
        return True

    elif board[1] == player and board[4] == player and board[7] == player:
        return True

    elif board[2] == player and board[5] == player and board[8] == player:
        return True

    # Check diagonals
    elif board[0] == player and board[4] == player and board[8] == player:
        return True

    elif board[2] == player and board[4] == player and board[6] == player:
        return True

    else:
        return False


# Function to check draw
def check_draw():

    if " " not in board:
        return True

    else:
        return False


# Start with Player X
current_player = "X"

# Game loop
while True:

    # Show board
    display_board()

    # Ask player for position
    position = int(input("Player " + current_player + ", enter position (1-9): "))

    # Convert to list index
    index = position - 1

    # Check if position is empty
    if board[index] == " ":

        # Place player symbol
        board[index] = current_player

        # Check winner
        if check_winner(current_player):

            display_board()

            print("Player " + current_player + " wins!")

            break

        # Check draw
        elif check_draw():

            display_board()

            print("The game is a draw!")

            break

        # Switch player
        if current_player == "X":
            current_player = "O"

        else:
            current_player = "X"

    else:
        print("Position already taken! Try again.")