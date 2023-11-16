def solveSudoku(board):
    def is_valid(num, row, col):
        for i in range(9):
            if board[i][col] == num or board[row][i] == num:
                return False

        row_start, col_start = 3 * (row // 3), 3 * (col // 3)
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if board[i][j] == num:
                    return False
        return True

    def backtrack():
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    for num in map(str, range(1, 10)):
                        if is_valid(num, row, col):
                            board[row][col] = num
                            if backtrack():
                                return True
                            board[row][col] = "."
                    return False
        return True

    backtrack()

# Input Sudoku board
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

# Call the solveSudoku function with the input puzzle
solveSudoku(board)

# Print the solved Sudoku board
for row in board:
    print(" ".join(row))
