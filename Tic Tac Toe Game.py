def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    """Checks if the player has achieved a win."""
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    """Checks if the game is a draw."""
    for row in board:
        if any([cell == ' ' for cell in row]):
            return False
    return True

def tic_tac_toe():
    """Main function to run the Tic Tac Toe game."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        print(f"Player {players[turn % 2]}'s turn.")
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if board[row][col] == ' ':
            board[row][col] = players[turn % 2]
            if check_win(board, players[turn % 2]):
                print_board(board)
                print(f"Congratulations! Player {players[turn % 2]} wins!")
                break
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            turn += 1
        else:
            print("That position is already taken. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
