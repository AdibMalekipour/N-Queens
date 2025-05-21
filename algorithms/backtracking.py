def solve_n_queens(n):
    board = [-1] * n
    solutions = []

    def is_safe(row, col):
        for prev_row in range(row):
            if board[prev_row] == col or abs(board[prev_row] - col) == abs(prev_row - row):
                return False
        return True

    def solve(row=0):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1

    solve()
    return solutions[0] if solutions else []
