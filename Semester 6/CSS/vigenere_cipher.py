import string

char_num_map = {j: i for i, j in enumerate(string.ascii_lowercase + " ")}
num_char_map = {i: j for i, j in enumerate(string.ascii_lowercase + " ")}


def encrypt(text, key):
    encrypted = ""
    text = text.lower()
    key = key.lower()

    key_counter = 0

    for i in text:
        rotation = char_num_map[i] + char_num_map[key[key_counter]]
        C = num_char_map[rotation % vocab_size]
        encrypted += C
        if(key_counter == len(key) - 1):
            key_counter = 0
        else:
            key_counter += 1
    return encrypted


def decrypt(text, key):
    decrypted = ""
    text = text.lower()
    key = key.lower()

    key_counter = 0

    for i in text:
        rotation = char_num_map[i] - char_num_map[key[key_counter]]
        C = num_char_map[rotation % vocab_size]
        decrypted += C
        if(key_counter == len(key) - 1):
            key_counter = 0
        else:
            key_counter += 1
    return decrypted


if __name__ == "__main__":
    vocab_size = len(string.ascii_lowercase + " ")
    message = input("Enter text: ")
    key = input("Enter single word key: ")

    encrypted_message = encrypt(message, key)
    decrypted_message = decrypt(encrypted_message, key)
    print(encrypted_message)
    print(decrypted_message)
