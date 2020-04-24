import hashlib
# encoding string using md5 hash function
BYTE_STRING = hashlib.md5(b"This is MD5 in byte equivalent")
# printing the equivalent byte value.
print("The byte equivalent of hash is : ", end="")
print(BYTE_STRING.digest())
HEX_STRING = "This is MD5 in Hex equivalent"
# encoding string using encode()
# then sending to md5()
HEX = hashlib.md5(HEX_STRING.encode())
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end="")
print(HEX.hexdigest())


# -------------------
print("\n\n==================")
print("USING SHA-1")
print("==================")


# initializing string
string = "USING SHA-1 Algorithm"
# encoding string using encode()
# then sending to SHA1()
result = hashlib.sha1(string.encode())
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())
