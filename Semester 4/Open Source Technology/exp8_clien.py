import socket

s = socket.socket()
port = 12345
s.connect(('127.0.0.1', port))
message = s.recv(1024)
print(message.decode("utf-8"))
s.close()
