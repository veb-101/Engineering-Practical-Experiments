from copy import deepcopy as dc
from numpy import ravel as flatten
import heapq

# Helper functions


def getInvCount(array):
    count = 0
    for i in range(N * N - 1):
        for j in range(i + 1, N * N):
            if array[j] and array[i] and array[i] > array[j]:
                count += 1
    return count


def blankTilePosition(puzzle):
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if puzzle[i][j] == 0:
                return N - i, j


def isSolvable(puzzle):
    puzz = puzzle[:]
    invCount = getInvCount(flatten(puzz))
    if N % 2:
        return not invCount % 2  # return even
    else:
        pos = blankTilePosition(puzzle)[0]
        if pos % 2:  # X on odd row from last
            return not invCount % 2  # invCount is even
        else:
            return bool(invCount % 2)  # invCount is odd


def printMatrix(puzzle):
    for i in range(N):
        for j in range(N):
            print(f"{puzzle[i][j]}", end=" ")
        print()
    print()


def calculateCost(initital, final):
    cost = 0
    for i in range(N):
        for j in range(N):
            if initital[i][j] and initital[i][j] != final[i][j]:
                cost += 1
    return cost


def moveSafe(x, y):
    return x >= 0 and x < N and y >= 0 and y < N


def printPath(root):
    if root == None:
        return
    printPath(root.parent)
    printMatrix(root.board)
    print()


# Creating tree Nodes


class Node(object):
    def __init__(self, board, x, y, parent=None):
        self.board = board
        self.parent = parent
        self.x = x
        self.y = y
        self.level = 0
        self.cost = 0

    def __lt__(self, other):
        return (self.cost + self.level) < (other.cost + other.level)


def NewNode(mat, x, y, newX, newY, level, parent):
    curr = dc(mat)
    node = Node(curr, x, y, parent)
    node.board[x][y], node.board[newX][newY] = node.board[newX][newY], node.board[x][y]
    node.x = newX
    node.y = newY
    node.level = level
    return node


def solve(initial, x, y, final):
    queue = []
    root = NewNode(initial, x, y, x, y, 0, None)
    root.cost = calculateCost(initial, final)
    heapq.heapify(queue)
    heapq.heappush(queue, root)

    while len(queue) != 0:
        minCostNode = heapq.heappop(queue)
        if minCostNode.cost == 0:
            printPath(minCostNode)
            return
        for i in range(4):
            if moveSafe(minCostNode.x + row[i], minCostNode.y + col[i]):
                child = NewNode(minCostNode.board, minCostNode.x, minCostNode.y,
                                minCostNode.x + row[i], minCostNode.y + col[i],
                                minCostNode.level + 1, minCostNode)
                child.cost = calculateCost(child.board, final)
                heapq.heappush(queue, child)


if __name__ == "__main__":

    # bottom, left, top, right
    row = (1, 0, -1, 0)
    col = (0, -1, 0, 1)

    N = 4
    initial = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [0, 10, 11, 12],
        [9, 13, 14, 15]
    ]

    final = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]

    x, y = blankTilePosition(initial) # blank tile position
    x = N - x

    if isSolvable(initial):
        solve(initial, x, y, final)
    else:
        print("This initial arrangement cannot be solved")
