import string


full_alphabets = string.ascii_lowercase

char_num_map = {j:i for i, j in enumerate(full_alphabets)}
num_char_map = {i:j for i, j in enumerate(full_alphabets)}


def substitutionCipher(text):

    '''
    Uses AutoKey Cipher
    input{ 
        text : plaintext
    }
    '''

    text = text.lower().replace(" ", "")
    key = 12
    P = [char_num_map[i] for i in text]
    
    C = P[:]
    C.insert(0, key)
    C = C[:-1]
    
    cipher_text = ''
    
    for i, j in zip(P, C):
        cipher_text += num_char_map[(i + j)%26]

    return cipher_text


def transpositionKey(text):

    '''
    Uses Rail Fence Cipher
    input{ 
        text : text encrypted with a substitution cipher
    }
    '''

    text = text.lower().replace(" ", "")
    one, two = [], []

    for i, j in enumerate(text):
        if i % 2 == 0:
            one.append(j)
        else:
            two.append(j)
    
    cipher_text = "".join(one)
    cipher_text += "".join(two)

    return cipher_text


plaintext= input("Enter plain text: ")

cipher_text = transpositionKey(substitutionCipher(plaintext))
print(f"Cipher text: {cipher_text}")