import socket


def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print("Server Started.")
    while True:
        data, addr = s.recvfrom(1024)
        print(f"message From: {addr[1]} -> {data.decode('utf-8')}")
        data = input(("Reply => "))
        # data = f"Thanks for connecting, user {addr[1]}"
        s.sendto(data.encode("utf-8"), addr)

    s.close()


if __name__ == '__main__':
    Main()
