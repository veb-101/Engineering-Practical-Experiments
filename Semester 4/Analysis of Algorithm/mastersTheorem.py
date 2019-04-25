# not complete
from math import log

print("Enter coefficient values of eqn a(T(n/b) * n^p * log(n)^k")
a = int(input("Enter a for the given recurrence eqn: "))
b = int(input("Enter b for the given recurrence eqn: "))
p = int(input("Enter p for the given recurrence eqn: "))
k = int(input("Enter k for the given recurrence eqn: "))
# fn = eval(fn)

n_log_a_b = log(a, b)
if n_log_a_b > p:
    print("Case 1: slower growth")
    print(f"E:{n_log_a_b - p}")
    print(f"Solution:Theta(n ^{n_log_a_b})")

if n_log_a_b < p:
    print("Case 3: Faster growth")
    print(f"Solution:Theta(n ^{p})")

if n_log_a_b == p:
    print("Case 2: Same growth")
    print(f"Solution: Theta(n^{n_log_a_b}*log(n)^{k+1})")
