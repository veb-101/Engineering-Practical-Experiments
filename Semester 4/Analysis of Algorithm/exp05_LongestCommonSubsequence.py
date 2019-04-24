def longestCommonSequence(matrixValues, operations, sequenceA, sequenceB):
    for row in range(1, len(sequenceB)):
        for column in range(1, len(sequenceA)):
            if sequenceB[row] == sequenceA[column]:
                matrixValues[row][column] = matrixValues[row - 1][column - 1] + 1
                operations[row][column] = "d"
            else:
                val1, op1 = matrixValues[row - 1][column], "t"
                val2, op2 = matrixValues[row][column - 1], "l"
                if val1 >= val2:
                    matrixValues[row][column] = val1
                    operations[row][column] = op1
                else:
                    matrixValues[row][column] = val2
                    operations[row][column] = op2


def backtrack(op, sequence, row, column):
    letters = []
    while row > 0 and column > 0:
        if op[row][column] == "d":
            letters.append(sequence[column])
            row -= 1
            column -= 1
        elif op[row][column] == "l":
            column -= 1
        else:
            row -= 1
    return letters


if __name__ == "__main__":
    sequenceA = list(input("Enter sequence one: "))
    sequenceB = list(input("Enter sequence two: "))
    sequenceA.insert(0, "0")
    sequenceB.insert(0, "0")

    # For saving the values of the matrix
    matrixValues = [[0 for x in range(len(sequenceA))] for y in range(len(sequenceB))]
    # For savinf the operations done in each cell of matrixValues
    operations = [["X" for x in range(len(sequenceA))] for y in range(len(sequenceB))]

    # or
    # matrixValues = [[]] * len(sequenceB)
    # for i in range(len(sequenceB)):
    #     matrixValues[i] = [0] * len(sequenceA)
    #
    # operations = [[]] * len(sequenceB)
    # for i in range(len(sequenceB)):
    #     operations[i] = ["X"] * len(sequenceA)

    longestCommonSequence(matrixValues, operations, sequenceA, sequenceB)
    longestSequenceLength = matrixValues[len(sequenceB) - 1][len(sequenceA) - 1]

    row, column = len(sequenceB) - 1, len(sequenceA) - 1
    letter = backtrack(operations, sequenceA, row, column)
    sequence = "".join(reversed(letter))

    # optional
    # for i in range(1, len(sequenceB)):
    #     for j in range(1, len(sequenceA)):
    #         print(f"{matrixValues[i][j]}", end= " ")
    #     print()
    # print()
    # for i in range(1, len(sequenceB)):
    #     for j in range(1, len(sequenceA)):
    #         print(f"{operations[i][j]}", end=" ")
    #     print()
    print(f"Longest common sequence length is: {longestSequenceLength}")
    print(f"Sequence is: '{sequence}'")
