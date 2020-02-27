from math import gcd
from random import choice
import string
# step 1: select any two large prime numbers

# p, q = map(int, input("Enter prime numbers: ").split())
p, q = 2, 13
# step 2: Compute n = p*q

n = p * q

# step 3: phi(n) = (p - 1) * (q - 1)
phi_n = (p - 1) * (q - 1)

# step 4: select 'e' such that 1 < e < phi_n
# and gcd(e, phi_n) = 1
e = []
for i in range(2, phi_n):
    if gcd(i, phi_n) == 1: 
        e.append(i)

e = choice(e)
public_key = (e, n)

# step 5: select 'd' such that 1 < d < phi_n
# and d = e-1 mod phi_n or e*d = 1 mod phi_n or d = (1 + k * phi_n ) / n

k = range(0, phi_n)
d = []
for i in k:
    temp = (1 + i * phi_n) / e
    if temp % 1 == 0 and temp in k:
        d.append(int(temp))

d = d[0]

char_int_mapping = {j: i for i, j in enumerate(string.ascii_lowercase)}

int_char_mapping = {i: j for i, j in enumerate(string.ascii_lowercase)}

alphabets = string.ascii_lowercase
# step 6: Encryption

# plain_text = input("Enter text: ")
plain_text = "test wow"

plain_text = plain_text.lower().replace(" ", "")
plain_text_num = ""
cipher_text = []
for i in plain_text:
    plain_text_num += str(char_int_mapping[i])

plain_text_num = int(plain_text_num)

