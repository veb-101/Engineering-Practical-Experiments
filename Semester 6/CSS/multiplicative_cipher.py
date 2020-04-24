import string
from math import gcd

char_num_map = {j: i for i, j in enumerate(string.ascii_lowercase + " ")}
num_char_map = {i: j for i, j in enumerate(string.ascii_lowercase + " ")}


def encrypt(text, key):
    encrypted = ""
    text = text.lower()
    for letter in text:
        letter_key = char_num_map[letter]
        rotation = (letter_key * key) % 27
        encrypted += num_char_map[rotation]
    return encrypted


def modInverse(a, m):
    if gcd(a, m) == 1:
        a = a % m
        for x in range(1, m):
            if ((a * x) % m == 1):
                return x
        return 1


def decrypt(text, key):
    decrypted = ""
    key = modInverse(key, 27)
    text = text.lower()
    for letter in text:
        letter_key = char_num_map[letter]
        rotation = (letter_key * key) % 27
        decrypted += num_char_map[rotation]
    return decrypted


if __name__ == "__main__":
    message = input("Enter text: ")
    encrypted_message = encrypt(message, 5)
    decrypted_message = decrypt(encrypted_message, 5)
    print(encrypted_message)
    print(decrypted_message)
