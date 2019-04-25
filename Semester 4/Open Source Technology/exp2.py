print("If-elif-else example -->")
a = input("\nEnter first number: ")
b = input("Enter second number: ")
c = input("Enter third number: ")

if (a > b and a > c):
    print(f"{a} is greatest!")
elif(b > a and b > c):
    print(f"{b} is greatest!")
else:
    print(f"{c} is greatest!")


print("\nFor example -->")
for i in range(0, 20, 2):  # start, stop, step
    print(i)

print("\n\nWhile example -->")
print("Even Numbers")
n = 0
while(n <= 20):
    if(n % 2 == 0):
        print(n, end=" ")
    n = n+1
