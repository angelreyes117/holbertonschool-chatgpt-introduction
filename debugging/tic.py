#!/usr/bin/python3

def print_board(board):
    """
    Prints the Tic-Tac-Toe board.
    
    Parameters:
    board (list): A 3x3 list representing the game board.
    
    Returns:
    None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner in the Tic-Tac-Toe game.

    Parameters:
    board (list): A 3x3 list representing the game board.

    Returns:
    str: The winning player ("X" or "O") if there's a winner, otherwise None.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    """
    Checks if the Tic-Tac-Toe board is full.

    Parameters:
    board (list): A 3x3 list representing the game board.

    Returns:
    bool: True if the board is full, otherwise False.
    """
    return all(cell != " " for row in board for cell in row)

def get_valid_input(prompt):
    """
    Gets a valid input from the user within the range 0-2.

    Parameters:
    prompt (str): The prompt message for the user.

    Returns:
    int: A valid integer input (0, 1, or 2).
    """
    while True:
        try:
            value = int(input(prompt))
            if value in [0, 1, 2]:
                return value
            else:
                print("Invalid input! Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input! Please enter a number (0, 1, or 2).")

def tic_tac_toe():
    """
    Runs the Tic-Tac-Toe game loop.

    Returns:
    None
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        
        # Get valid row and column input
        row = get_valid_input(f"Enter row (0, 1, or 2) for player {player}: ")
        col = get_valid_input(f"Enter column (0, 1, or 2) for player {player}: ")

        if board[row][col] == " ":
            board[row][col] = player
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            
            # Switch player
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()
