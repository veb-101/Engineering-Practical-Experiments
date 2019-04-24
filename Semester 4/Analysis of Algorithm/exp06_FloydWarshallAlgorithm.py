def floyd_war(matrixSize, adjMatrix):
    D_old = adjMatrix[:]
    D_new = [[0 for x in range(matrixSize)] for y in range(matrixSize)]

    print(f"Via node 0: ")
    for row in range(matrixSize):
        for column in range(matrixSize):
            print(D_old[row][column], end=" ")
        print()
    print()

    for node in range(matrixSize):
        print(f"Via Node {node + 1}:")
        for row in range(matrixSize):
            for column in range(matrixSize):
                value = min(D_old[row][column], D_old[row][node] + D_old[node][column])
                D_new[row][column] = test if value > 90 else value
                print(D_new[row][column], end=" ")
            print()
        D_old = D_new[:]
        print()


if __name__ == "__main__":
    matrixSize = int(input("Enter adjacency matrix size: "))
    print("Enter Adjacency matrix values for vertices other than diagonals...")

    adjMatrix = [[int(input(f"Enter value for {row + 1, column + 1}:")) if column != row else 0
                  for column in range(matrixSize)]for row in range(matrixSize)]

    test = float("inf")
    adjMatrix = [[test if adjMatrix[i][j] >= 90 else adjMatrix[i][j] for j in range(matrixSize)]
                 for i in range(matrixSize)]

    print()
    floyd_war(matrixSize, adjMatrix)
