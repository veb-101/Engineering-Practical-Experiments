import string

char_num_map = {j: i for i, j in enumerate(string.ascii_lowercase + " ")}
num_char_map = {i: j for i, j in enumerate(string.ascii_lowercase + " ")}


def encrypt(text, key):
    encrypted = ""
    text = text.lower()
    for letter in text:
        letter_key = char_num_map[letter]
        rotation = (letter_key + key) % vocab_size
        encrypted += num_char_map[rotation]
    return encrypted


def decrypt(text, key):
    decrypted = ""
    text = text.lower()
    for letter in text:
        letter_key = char_num_map[letter]
        rotation = (letter_key - key) % vocab_size
        decrypted += num_char_map[rotation]
    return decrypted


if __name__ == "__main__":
    vocab_size = len(string.ascii_lowercase + " ")
    message = input("Enter text: ")
    encrypted_message = encrypt(message, 3)
    decrypted_message = decrypt(encrypted_message, 3)
    print(encrypted_message)
    print(decrypted_message)
