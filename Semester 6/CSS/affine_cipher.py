import string
from math import gcd

char_num_map = {j: i for i, j in enumerate(string.ascii_lowercase + " ")}
num_char_map = {i: j for i, j in enumerate(string.ascii_lowercase + " ")}


def encrypt(text, key):
    encrypted = ""
    multiply_key = key[0]
    addition_key = key[1]
    text = text.lower()

    for letter in text:
        letter_key = char_num_map[letter]
        multiplication = (letter_key * multiply_key) % vocab_size
        addition = (multiplication + addition_key) % vocab_size
        encrypted += num_char_map[addition]
    return encrypted


def multiplicative_inverse(a, m):
    if gcd(a, m) == 1:
        a = a % m
        for x in range(1, m):
            if ((a * x) % m == 1):
                return x
        return 1


def additive_inverse(a, m):
    return (-a + m) % m


def decrypt(text, key):
    decrypted = ""
    multiply_key = key[0]
    addition_key = key[1]

    multiply_key_inv = multiplicative_inverse(multiply_key, vocab_size)
    addition_key_inv = additive_inverse(addition_key, vocab_size)

    text = text.lower()
    for letter in text:
        letter_key = char_num_map[letter]
        addition = (letter_key + addition_key_inv) % vocab_size
        multiplication = (addition * multiply_key_inv) % vocab_size
        decrypted += num_char_map[multiplication]

    return decrypted


if __name__ == "__main__":
    vocab_size = len(string.ascii_lowercase + " ")
    message = input("Enter text: ")
    encrypted_message = encrypt(message, (7, 2))
    decrypted_message = decrypt(encrypted_message, (7, 2))
    print(encrypted_message)
    print(decrypted_message)
