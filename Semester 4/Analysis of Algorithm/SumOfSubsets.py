# Credits: StackOverflow, where else....
# https://stackoverflow.com/questions/29456502/subset-sum-with-backtracking-on-python
# done with the help of generators
# might be useful to learn about them before jumping in


def sumOfSubset(array, num):
    if num < 0:
        return
    if len(array) == 0:
        if num == 0:
            yield []
        return

    # element not selected
    for solution in sumOfSubset(array[1:], num):
        yield solution

    # element selected
    for solution in sumOfSubset(array[1:], num - array[0]):
        yield [array[0]] + solution


if __name__ == '__main__':
    sum = int(input("Enter final sum: "))
    count = int(input("Enter number of elements: "))
    numbers = []
    for i in range(count):
        addNum = int(input("Enter number: "))
        numbers.append(addNum)
    numbers.sort()

    # numbers = [int(input(f"Enter number {i+1}: ")) for i in range(10)]
    # numbers = list(range(1, 11))

    print(list(sumOfSubset(numbers, sum)))
