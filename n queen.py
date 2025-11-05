# N-Queens problem using backtracking (with first Queen placed by user)

def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()

def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row, n):
    if row == n:
        return True  # All queens placed

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens(board, row + 1, n):
                return True
            board[row][col] = 0  # backtrack
    return False

# Main program
n = int(input("Enter the number of Queens (N): "))

# Initialize board
board = [[0] * n for _ in range(n)]

# Get first Queen position from user
row1 = int(input("Enter row index for first Queen (0-based): "))
col1 = int(input("Enter column index for first Queen (0-based): "))
board[row1][col1] = 1  # place first queen

# Start solving from the next row
if solve_n_queens(board, row1 + 1, n):
    print("\nFinal N-Queens solution:")
    print_board(board)
else:
    print("No solution possible with that first queen position.")
