import random

n, g = list(map(int, input("Enter prime numbers: ").split()))

def checkPrime(n):
    if n <= 0:
        return False
    else:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
    return True 

def mix(a, b):
    return checkPrime(a) and checkPrime(b)

while not mix(n, g):
    print("Input Prime numbers...")
    n, g = list(map(int, input("Enter prime numbers: ").split()))
    

x = random.randint(0, 1) * 1000

y = random.randint(0, 2) * 1000

A = (g ** x) % n
B = (g ** y) % n

k1 = (B ** x) % n
k2 = (A ** y) % n

print(f"A -> {A}: key -> {k1}")
print(f"B -> {B}: key -> {k2}")

