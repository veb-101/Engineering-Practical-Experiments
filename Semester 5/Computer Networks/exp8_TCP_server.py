import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")
port = 12345
s.bind(('', port))
print(f"socket binded to {port}")
s.listen(5)
print("socket is listening")
while True:
    c, addr = s.accept()
    # print(c) # socket information
    print('Got connection from', addr)
    c.send('Thank you for connecting'.encode("utf-8"))
c.close()
