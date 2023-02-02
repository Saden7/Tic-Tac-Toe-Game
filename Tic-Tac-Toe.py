# Tic-Tac-Toe Game

# Initialize the board
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Function to print the board
def print_board():
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print()

# Function to check if there is a winner
def check_winner():
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]
    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    # Check if the board is full
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return None
    return 'Tie'

# Main game loop
player = 'X'
while True:
    print_board()
    x = int(input("Enter x coordinate (0-2): "))
    y = int(input("Enter y coordinate (0-2): "))
    if board[x][y] != ' ':
        print("This spot is already taken. Try again.")
        continue
    board[x][y] = player
    winner = check_winner()
    if winner:
        print_board()
        print(winner + " wins!")
        break
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
