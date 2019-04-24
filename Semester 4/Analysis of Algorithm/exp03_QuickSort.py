
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr if x < pivot]  # elements less than pivot in this list
    middle = [x for x in arr if x == pivot]  # elements equal to pivot in this list
    right = [x for x in arr if x > pivot]  # elements grater than pivot in this list
    return quicksort(left) + middle + quicksort(right)


if __name__ == "__main__":
    size = input("Enter size of arays: ")
    alist = [int(input(f"Enter number {i + 1}: ")) for i in range(int(size))]
    print(f"\nArray: {alist}")
    # # arr = [1, 2, 3, 0,24]
    # quicksort(arr)
    print(f"Sorted using Quick Sort: {quicksort(alist)}")


# Time Complexity: O(n*logn)
# quick sort is in place sorting algorithm
# quick sort is not stable
