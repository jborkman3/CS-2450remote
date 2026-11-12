import os

# Every set of three board positions that counts as a win:
# three rows, three columns, and two diagonals.
WINNING_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]


def clear_screen():
    """Clear the terminal (uses 'cls' on Windows, 'clear' elsewhere)."""
    os.system('cls' if os.name == 'nt' else 'clear')


def show_board(board):
    """Print the 3x3 board. Empty spots show their position number."""
    for row in range(3):
        start = row * 3
        print(f" {board[start]} | {board[start + 1]} | {board[start + 2]} ")
        if row < 2:
            print("---+---+---")


def draw_screen(board):
    """Clear the terminal and redraw the title and board."""
    clear_screen()
    print("Tic-Tac-Toe\n")
    show_board(board)


def find_winner(board):
    """Return 'X' or 'O' if that player has three in a line, otherwise None."""
    for first, second, third in WINNING_LINES:
        # All three spots must hold the same player's mark. Empty spots hold
        # different digits, so they can never all match each other.
        if board[first] == board[second] == board[third] and board[first] in ('X', 'O'):
            return board[first]
    return None


def play():
    """Run one game of two-player Tic-Tac-Toe in the terminal."""
    # Spots start as the digits '0'-'8' so players can see which number to pick.
    board = [str(position) for position in range(9)]
    current_player = "X"
    error_message = ""

    # Keep playing while there is at least one open (still numbered) spot.
    while any(spot.isdigit() for spot in board):
        draw_screen(board)

        # Show any error from the previous attempt after redrawing,
        # otherwise clearing the screen would erase it before it's seen.
        if error_message:
            print(f"\n{error_message}")
            error_message = ""

        print(f"\n{current_player}'s turn!")
        try:
            move = int(input("Pick a spot (0-8): "))
        except ValueError:
            error_message = "Invalid input. Please enter a number from 0 to 8."
            continue

        # Reject moves that are off the board or on a spot already taken.
        if not (0 <= move < 9 and board[move].isdigit()):
            error_message = "Spot is taken or out of range. Try again."
            continue

        board[move] = current_player

        winning_player = find_winner(board)
        if winning_player:
            draw_screen(board)
            print(f"\n{winning_player} wins!")
            return

        # Switch turns between X and O.
        current_player = "O" if current_player == "X" else "X"

    # The loop only ends without a winner when every spot is filled.
    draw_screen(board)
    print("\nIt's a draw!")


if __name__ == "__main__":
    play()
