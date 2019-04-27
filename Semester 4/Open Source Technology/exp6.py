# Stack
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

# Queue


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


# Linked list
class Node(object):
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    @property
    def getData(self):
        return self.data

    @getData.setter
    def setData(self, newdata):
        self.data = newdata

    @property
    def getNext(self):
        return self.next

    @getNext.setter
    def setNext(self, newnext):
        self.next = newnext


class LinkedList(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext = self.head
        self.head = temp

    @property
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData == item:
                found = True
            else:
                current = current.getNext

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData == item:
                found = True
            else:
                previous = current
                current = current.getNext
        if previous == None:
            self.head = current.getNext
        else:
            previous.setNext = current.getNext

    def printList(self):
        current = self.head
        while current != None:
            print(f"{current.data} -->", end="")
            current = current.getNext
        print("None")


print("-----------Stack------------")
s = Stack()
print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())

print("-----------Queue------------")
q = Queue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
print(f"Removed --> {q.dequeue()}")
print(f"Removed --> {q.dequeue()}")
print(q.size())

print("---------LinkedList-----------")
myList = LinkedList()
myList.add(31)
myList.add(77)
myList.add(17)
myList.add(93)
myList.add(26)
myList.add(54)
print(myList.size)
print(myList.search(17))
myList.printList()
myList.remove(93)
myList.remove(54)
myList.printList()
