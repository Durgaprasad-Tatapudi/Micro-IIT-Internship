def print_board(board):
    """Prints the Tic-Tac-Toe board in a clear 3x3 format."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)  # Separator between rows


def check_winner(board, player):
    """Checks if the given player has won the game."""
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Check row
            return True
        if all(board[j][i] == player for j in range(3)):  # Check column
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_draw(board):
    """Checks if the game is a draw (no empty spaces left)."""
    return all(cell in ('X', 'O') for row in board for cell in row)


def get_valid_input(board):
    """Gets a valid move from the user."""
    while True:
        try:
            row, col = map(int, input("Enter row and column (0-2, space-separated): ").split())
            if row in range(3) and col in range(3):
                if board[row][col] == " ":
                    return row, col
                else:
                    print("Cell already occupied! Choose another.")
            else:
                print("Invalid input! Enter numbers between 0 and 2.")
        except ValueError:
            print("Invalid input! Please enter two numbers separated by space.")


def play_game():
    """Runs the Tic-Tac-Toe game loop."""
    board = [[" " for _ in range(3)] for _ in range(3)]  # 3x3 board
    current_player = "X"

    while True:
        print_board(board)  # Display board before each move
        print(f"Player {current_player}'s turn.")

        # Get valid move
        row, col = get_valid_input(board)
        board[row][col] = current_player  # Place player's mark

        # Check for a win
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins! 🎉")
            break

        # Check for a draw
        if is_draw(board):
            print_board(board)
            print("It's a draw! 🤝")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


# Run the game
if __name__ == "__main__":
    play_game()
