
minimum = 9999
maximum = 0


def MinMax(array, start, end):
    global minimum
    global maximum
    # divide
    if end - start > 2:
        middle = (start + end)//2
        MinMax(array, start, middle)
        MinMax(array, middle, end)
    # conquer
    else:
        array = array[start:end]
        if end - start == 1:
            # when only one element is present
            # min and max are the same element
            min1 = array[0]
            max1 = array[0]
        elif (end - start) == 2:
            # when 2 elements are present in the array
            min1 = min(array[0], array[1])
            max1 = max(array[0], array[1])

        minimum = min(minimum, min1)
        maximum = max(maximum, max1)


if __name__ == "__main__":
    size = int(input("Enter size of array: "))
    array = []
    for i in range(int(size)):
        array.append(int(input(f"Enter element {i + 1}: ")))
    print(F"Array is: {array}")

    MinMax(array, 0, size)
    print(f"Maximum is: {maximum}")
    print(f"Minimum is: {minimum}")
