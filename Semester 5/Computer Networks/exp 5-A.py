# hamming code for 7-bit data - Naive implementation
dataword = list(input("Enter 7-bit dataword: "))
dataword = list(map(int, dataword))
# dataword = [1, 0, 0, 1, 1, 0, 1]
check_bits_len = 4
check_bit_positions = [0, 1, 3, 7]  # 1, 2, 4, 8
parity_check_bits = [
    [0, 2, 4, 6, 8, 10],
    [1, 2, 5, 6, 9, 10],
    [3, 4, 5, 6],
    [7, 8, 9, 10]
]
codeword = dataword[:]


def parityBitValue(check_bits, word=codeword):
    total = 0
    for positions in check_bits:
        total += word[positions]
    return 1 if total % 2 else 0

def retreiveDataWord():
    dataword = ""
    for i in range(len(codeword)):
        if i not in check_bit_positions:
            dataword += str(codeword[i])
    return dataword

# ---------------------------
# Creating codeword
for i in check_bit_positions:
    codeword.insert(i, f"c{i}")


for i in parity_check_bits:
    bit_no = i[0]
    codeword[bit_no] = parityBitValue(i[1:])

print(f"Dataword: {''.join(map(str,dataword))}")
print(f"Codeword: {''.join(map(str,codeword))}")

# ------------------------
# introduce error in codeword
# ------------------------

error_bit = int(input("Introduce error in bit (1-11): "))
# inversing bit 6
codeword[error_bit - 1] ^= 1
print(f"Codeword: {''.join(map(str,codeword))}")
print("\nError checking...")

error_word = ''

for i in reversed(parity_check_bits):
    error_word += f"{parityBitValue(i)}"

dec_error_word = int(error_word, 2)

if dec_error_word > 0:
    print(f"Error detected at bit: {dec_error_word}.")
    print(f"Inverting bit {dec_error_word} to correct the error...")
    print(
        f"Bit {error_bit}: {codeword[dec_error_word - 1]} -> {codeword[dec_error_word - 1] ^ 1}")
    codeword[dec_error_word - 1] ^= 1
    print(f"Corrected code word: {''.join(map(str,codeword))}")
    print(f"Retrived Dataword: {retreiveDataWord()}")

    
else:
    print(f"No error detected.")
    print(f"Retrived Dataword: {retreiveDataWord()}")
