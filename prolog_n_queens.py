def is_safe(board, row, col, n):
    # Check this column
    for i in range(row):
        if board[i] == col:
            return False
    
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        solutions.append(board.copy())
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens_util(board, row + 1, n, solutions)
            

def solve_n_queens(n):
    board = [-1] * n  
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions

def print_solutions(solutions, n):
    for idx, solution in enumerate(solutions):
        print(f"Solution {idx + 1}:")
        for row in range(n):
            line = ""
            for col in range(n):
                if solution[row] == col:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print()


n = 4
solutions = solve_n_queens(n)
print(f"Total solutions for {n}-Queens: {len(solutions)}")
print_solutions(solutions, n)
