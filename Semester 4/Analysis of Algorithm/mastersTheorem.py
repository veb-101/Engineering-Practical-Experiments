# not complete
from math import log

a = int(input("Enter a for the given recurrence eqn: "))
b = int(input("Enter b for the given recurrence eqn: "))
n = int(input("Enter n for the given recurrence eqn: "))
fn = input("Enter expression in terms of n: ")
fn = eval(fn)

n_log_a_b = n ** (log(a, b))
print(fn, n_log_a_b)
if fn < n_log_a_b:
    print("This is case I")
    e = 1
    new_fn = n ** (log(a, b) - e)
    while new_fn != fn:
        e += 1
        new_fn = n ** (log(a, b) - e)

    print("T(n): {}".format(n ** (log(a, b))))

elif fn == int(n_log_a_b):
    print("This is case II")
    k = 0
    new_fn = (n ** log(a, b)) * log(n)**k
    print(new_fn)
    while new_fn != fn:
        k += 1
        new_fn = (n ** log(a, b)) * log(n) ** k
    print(k)
    print(f"T(n): {(n ** log(a,b)) * (log(n))**k+1 }")
