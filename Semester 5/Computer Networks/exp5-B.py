# Credits:
# 1) https://gist.github.com/evansneath/4650991
# 2) https://www.tutorialspoint.com/How-to-convert-string-to-binary-in-Python


def crc(msg, div, code='000'):
    # Append the code to the message. If no code is given, default to '000'
    msg = msg + code

    # Convert msg and div into list form for easier handling
    msg = list(msg)
    div = list(div)
    # Loop over every message bit (minus the appended code)
    for i in range(len(msg)-len(code)):
        # If that messsage bit is 1, perform modulo 2 multiplication
        if msg[i] == '1':
            for j in range(len(div)):
                # Perform modulo 2 multiplication on each index of the divisor
                msg[i+j] = str((int(msg[i+j])+int(div[j])) % 2)

    # Output the last error-checking code portion of the message generated
    return ''.join(msg[-len(code):])


# TEST 1 ####################################################################
print("Sender's side....")
# Use a divisor that simulates: x^3 + x + 1
div = '1011'
msg = input('Enter message: ')
msg = ''.join(format(ord(x), 'b') for x in msg)

print(f'Binary encoded input message: {msg}')
print(f'Binary encoded G(x): {div}')

code = crc(msg, div)
print(f"Remaider calculated at sender's side: {code}")


print("\nReceiver's side....")


def printCheck(msg, div, code):
    remainder = crc(msg, div, code)
    print(f'Remainder is: {remainder}')
    print('Success:', remainder == '000')


def errorFunc(msg, div, code):
    Error = input("Introduce error(T/F): ")
    if Error in ('T', 't'):
        msg = list(msg)
        msg[7] = str(int(msg[7], 2) ^ 1)
        msg = ''.join(msg)
        printCheck(msg, div, code)
    else:
        printCheck(msg, div, code)


errorFunc(msg, div, code)
