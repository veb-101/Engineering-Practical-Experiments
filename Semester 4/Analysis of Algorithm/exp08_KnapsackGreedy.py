def fractionalKnapsack(matrix, n, bagCap):
    selected = []
    i, profit, inside = 0, 0, 0
    while i < n and bagCap > 0:
        item = matrix[i]
        number = item[0]
        value = item[1]
        weight = item[2]
        if bagCap >= weight:
            profit += value
            selected.append(number)
            inside += 1
            bagCap -= weight
        elif bagCap < weight:
            profit += (value * bagCap / weight)
            inside += bagCap / weight
            selected.append(number)
            bagCap = 0

        i += 1
    print(f"Total items inside: {inside}")
    print(f"Total Weight remaining: {bagCap}")
    print(f"Total Profit: {profit}")


if __name__ == "__main__":
    n = int(input("Enter number of items: "))
    bagCap = int(input("Enter bag size: "))
    matrix = []
    for i in range(n):
        p = int(input(f"Enter profit for item {i+1}: "))
        w = int(input(f"Enter weight for item {i+1}: "))
        profitPerWeight = round(p / w, 2)
        matrix.append([i, p, w, profitPerWeight])

    matrix.sort(key=lambda x: x[3], reverse=True)
    fractionalKnapsack(matrix, n, bagCap)
