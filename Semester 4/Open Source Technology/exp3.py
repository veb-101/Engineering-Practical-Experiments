def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def subtract(a, b):
    return a - b


def divide(a, b):
    return a / b


print(f"Addition: {add(4, 5)}")
print(f"Subtraction{subtract(4, 5)}")
print("*" * 20)


class Animal():
    def __init__(self, animalName):
        print(animalName, 'is an animal.')

    def __str__(self):
        return "Main class"


class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)

    def __str__(self):
        return "Single Inheritance"


class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammalName):
        print(NonWingedMammalName, "can't fly.")
        super().__init__(NonWingedMammalName)

    def __str__(self):
        return "Multilevel Inheritance"


class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammalName):
        print(NonMarineMammalName, "can't swim.")
        super().__init__(NonMarineMammalName)

    def __str__(self):
        return "Multilevel Inheritance"


class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Dog has 4 legs.')
        super().__init__('Dog')

    def __str__(self):
        return "Multiple Inheritance"


# animal = Animal("Dog")
# mammal = Mammal("Dog")
# nonwinged = NonWingedMammal("Dog")
# nonmarine = NonMarineMammal("Dog")
d = Dog()
print(d)
# print(animal)
# # print(mammal)
# # print(nonwinged)
# # print(nonmarine)
print("*" * 20)
x = int(input("Enter x: "))
y = int(input("Enter y: "))
try:
    result = x // y
    print("Yeah ! Your answer is :", result)
except Exception as e:
    # print("Sorry ! You are dividing by zero ")
    print()
