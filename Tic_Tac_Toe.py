
# Simple Tic Tac Toe Game in Python

# Function to display the board
def display_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_draw(board):
    return all(cell != " " for row in board for cell in row)

# Main game function
def tic_tac_toe():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic Tac Toe!")
    display_board(board)

    # Game loop
    while True:
        # Get the current player's move
        print(f"Player {players[current_player]}'s turn:")
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
        except ValueError:
            print("Invalid input! Please enter numbers 0, 1, or 2.")
            continue

        # Validate the move
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = players[current_player]
            display_board(board)

            # Check if the player has won
            if check_winner(board, players[current_player]):
                print(f"Player {players[current_player]} wins!")
                break

            # Check for a draw
            if is_draw(board):
                print("It's a draw!")
                break

            # Switch players
            current_player = 1 - current_player
        else:
            print("Invalid move! The cell is already occupied or out of range. Try again.")

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
