import numpy as np


def encrypt(text, cols, rearrange):
    encrypted = []
    text = text.lower().replace(" ", "")

    text = text + "X" * (-len(text) % cols)

    text = np.array(list(text))
    text = text.reshape(-1, cols)
    permuted = np.zeros_like(text)

    for i, j in enumerate(rearrange):
        permuted[:, i] = text[:, j]

    # print(text, "\n", permuted)

    for i in range(cols):
        temp = list(permuted[:, i])
        encrypted += temp

    return "".join(encrypted)


def decrypt(text, cols, rearrange):
    decrypted = []
    text = text.lower().replace(" ", "")
    text = np.array(list(text))
    text = text.reshape(cols, -1)
    text = text.T
    permuted = np.zeros_like(text)

    for i, j in enumerate(rearrange):
        permuted[:, j] = text[:, i]

    # print(text, "\n", permuted)

    for i in range(text.shape[0]):
        temp = list(permuted[i])
        decrypted += temp

    decrypted = "".join(decrypted)
    decrypted = decrypted.replace("x", "")
    return decrypted


if __name__ == "__main__":
    message = input("Enter message: ")
    columns = int(input("Enter no. of cols: "))
    permutation_key = []

    for i in range(columns):
        permutation_key.append(
            int(input(f"Input new postion for col {i} (0-{columns - 1}): ")))

    encrypted_text = encrypt(message, columns, permutation_key)
    decrypted_text = decrypt(encrypted_text, columns, permutation_key)
    print(encrypted_text)
    print(decrypted_text)
