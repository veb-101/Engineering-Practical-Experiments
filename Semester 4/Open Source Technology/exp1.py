print("String example")
s = "this is a test String"
print(f"String: {s}")
print(f"String Capitalized: {s.capitalize()}")
print(f"String Finding index: {s.find('e')}")
print(f"String Lowercase: {s.lower()}")
print(f"String Uppercase: {s.upper()}")
print(f"String Length: {len(s)}")
print(f"String Replace: {s.replace('this', 'THIS')}")
print(f"String Swapcase: {s.swapcase()}")
print(f"String Title: {s.title()}")
print()

print("List examples")
L = ['C++', 'Java', 'Python']
print(f"List: {L}")
print(f"List slicing: {L[1:]}")
print(f"List slicing: {L[::-1]}")
print(f"List slicing: {L[0:2]}")
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"List: {L}")
L.append(10)
print(f"List Appending:{L}")
print(f"List Popping:{L.pop()}")
L.insert(4, 20)
print(f"List Inserting : {L}")  # position, value
L.reverse()
print(f"List Reversed: {L}")
L.sort()
reversed_list = reversed(L)
print("Reversed list: {}".format(reversed_list))
for i in reversed_list:
    print(i)
print(f"List Sorted: {L}")

print("\nTuple example")
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print(f"tup1[0]: {tup1[0]}")
print(f"tup2[1:5]: {tup2[1:5]}")
tup3 = tup1 + tup2
print(f"Creating new from existing: tup3: {tup3}")

print("\nDictionary examples")
d = {'Name': 'Test', 'Age': 99, 'Class': 'failed'}
print(f"Dicstionary d: {d}")
d['Age'] = 0  # update existing entry
d['School'] = "Under a tree"  # Add new entry
print(f"Updating d['Age']: {d['Age']}")
print(f"Updating d['School']: {d['School']}")
print(f"Dictionary d: {d}")
print(f"Get Qualification : {d.get('Qualification', 'NA')}")
print(f"Dictionary items: {d.items()}")
print(f"Dictionary keys: {d.keys()}")
print(f"Dictionary values: {d.values()}")

print("\nSets example")
my_set = {1, 3}
print(my_set)
my_set.add(2)  # add an element
print(my_set)
my_set.update([2, 3, 4])  # add multiple elements
print(my_set)
my_set.update([4, 5], {1, 6, 8})  # add list and set
print(my_set)
my_set.remove(6)
print(my_set)
my_set.pop()  # pop another random element
print(my_set)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A | B)  # Union or A.union(B)
print(A & B)  # Intersection or A.intersection(B)
print(A - B)  # Difference or A.difference(B)

A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
print(A.difference(B))
print(A | B)
print(A.add(3))  # Error
