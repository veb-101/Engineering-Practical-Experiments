import numpy as np
import string


def encrypt(text, rows):
    encrypted = []
    text = text.lower().replace(" ", "")
    text = text + "X" * (-len(text) % rows)
    text = np.array(list(text))
    text = text.reshape(-1, rows)
    text = text.T
    # print(text)
    for i in range(text.shape[0]):
        temp = list(text[i])
        encrypted += temp

    encrypted = "".join(encrypted)
    return encrypted


def decrypt(text, rows):
    decrypted = []
    text = text.lower().replace(" ", "")

    text = np.array(list(text))
    text = text.reshape(rows, -1)

    # print(text)
    for i in range(text.shape[1]):
        temp = list(text[:, i])
        decrypted += temp

    decrypted = "".join(decrypted)
    decrypted = decrypted.replace("x", "")

    return decrypted


if __name__ == "__main__":
    message = input("Enter message: ")
    rows = int(input("Enter no. of rows: "))
    # message = "test message"
    # rows = 4
    encrypted_text = encrypt(message, rows)
    decrypted_text = decrypt(encrypted_text, rows)
    print(encrypted_text)
    print(decrypted_text)
