## selection sort
def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1): 
        positionOfMax=0
        for location in range(1,fillslot+1): 
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location
        # SWAP
        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]


## Insertion sort
def insertionSort(c):
    for index in range(1,len(c)):
        currentvalue = c[index]
        position = index

        while position>0 and c[position-1]>currentvalue:
            c[position]=c[position-1]
            position = position-1

        c[position]=currentvalue


if __name__ == "__main__":        
        size = input("Enter size of arays: ")
        alist = [int(input(f"Enter number {i + 1}: ")) for i in range(int(size))]
        c =alist[:]
        print(f"\nArray: {alist}")
        selectionSort(alist)
        print(f"Sorted using Selection Sort: {alist}")
        insertionSort(c)
        print(f"Sorted using Insertion Sort: {c}")

# Output
# Enter size of arays: 5
# Enter number 1: 12
# Enter number 2: 11
# Enter number 3: 10
# Enter number 4: 22
# Enter number 5: 32

# Array: [12, 11, 10, 22, 32]
# Sorted using Selection Sort: [10, 11, 12, 22, 32]
# Sorted using Insertion Sort: [10, 11, 12, 22, 32]