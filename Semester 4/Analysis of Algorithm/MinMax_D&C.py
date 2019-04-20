minimum = 9999
maximum = 0


def MinMax(array, start, end):
    global minimum
    global maximum
    middle = (start + end)//2
    # divide
    if end - start > 2:
        MinMax(array, start, middle)
        MinMax(array, middle, end)
    # conquer
    else:
        array = array[start:end]
        if end - start == 1:
            array.append(array[0])
        minimum = min(minimum, min(array[0], array[1]))
        maximum = max(maximum, max(array[0], array[1]))


if __name__ == "__main__":
    size = int(input("Enter size of array: "))
    array = []
    for i in range(int(size)):
        array.append(int(input(f"Enter element {i + 1}: ")))
    print(F"Array is: {array}")

    MinMax(array, 0, size)
    print(f"Maximum is: {maximum}")
    print(f"Minimum is: {minimum}")
