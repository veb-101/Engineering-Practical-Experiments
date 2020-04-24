import numpy as np
import string


def encrypt(text, cols):
    encrypted = []
    text = text.lower().replace(" ", "")

    text = text + "X" * (-len(text) % cols)

    text = np.array(list(text))
    text = text.reshape(-1, cols)
    # print(text)
    for i in range(cols):
        temp = list(text[:, i])
        encrypted += temp

    return "".join(encrypted)


def decrypt(text, cols):
    decrypted = []
    text = text.lower().replace(" ", "")
    text = np.array(list(text))
    text = text.reshape(cols, -1)
    text = text.T
    # print(text)
    for i in range(text.shape[0]):
        temp = list(text[i])
        decrypted += temp

    decrypted = "".join(decrypted)
    decrypted = decrypted.replace("x", "")
    return decrypted


if __name__ == "__main__":
    message = input("Enter message: ")
    columns = int(input("Enter no. of cols: "))
    encrypted_text = encrypt(message, columns)
    decrypted_text = decrypt(encrypted_text, columns)
    print(encrypted_text)
    print(decrypted_text)
