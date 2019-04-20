from copy import deepcopy as dc


def getBoard(size):
    board = ["_"]*size
    for i in range(size):
        board[i] = ["_"]*size
    return board


def printSolutions(solutions, size):
    for sol in solutions:
        for row in range(size):
            for col in range(size):
                print(sol[row][col], end=" ")
            print()
        print()


def safe(board, row, col, size):
    for y in range(col):
        if board[row][y] == "Q":
            return False

    x, y = row, col
    while x >= 0 and y >= 0:
        if board[x][y] == "Q":
            return False
        x -= 1
        y -= 1

    x, y = row, col
    while x < size and y >= 0:
        if board[x][y] == "Q":
            return False
        x += 1
        y -= 1

    return True


def solve(board, col, size):
    global count
    # base case
    if col >= size:
        return
    for i in range(size):
        if safe(board, i, col, size):
            board[i][col] = "Q"
            if col == size-1 and count < 4:
                addSolution(board)
                count += 1
                board[i][col] = "_"
                return
            solve(board, col+1, size)
            # backtrack
            board[i][col] = "_"


def addSolution(board):
    global solutions
    saved_board = dc(board)
    solutions.append(saved_board)


size = 8
board = getBoard(size)
solutions = []
count = 0
solve(board, 0, size)
print(f"Solutions...")
printSolutions(solutions, size)
print(f"Printed solutions = {len(solutions)}")
