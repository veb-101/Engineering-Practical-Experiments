def mergeSort(alist):
    # dividing lists in halves
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        # merging
        i = 0
        j = 0
        k = 0
        # add elements in list by comparing elements in lefthalf and righthalf
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j+1
            k = k+1

        # if element still left in lefthalf
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1

        # if element still left in lefthalf
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1


if __name__ == "__main__":
    size = input("Enter size of arays: ")
    a = [int(input(f"Enter number {i + 1}: ")) for i in range(int(size))]
    # a = []
    # for i in range(int(size)):
    #     a.append(int(input(f"Enter number {i + 1}: ")))
    mergeSort(a)
    print(f"Array sorted using Merge Sort: {a}")

# Sample Output
# Enter size of arays: 5
# Enter number 1: 12
# Enter number 2: 1
# Enter number 3: 221
# Enter number 4: 11
# Enter number 5: 2
# Array sorted using Merge Sort: [1, 2, 11, 12, 221]
