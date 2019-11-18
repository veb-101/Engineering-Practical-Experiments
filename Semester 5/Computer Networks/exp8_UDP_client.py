import socket


def Main():

    # The UDP echo client is similar the server, but does not use bind() to
    # attach its socket to an address. It uses sendto() to deliver its
    # message directly to the server, and recvfrom() to receive the response.
    server = ('127.0.0.1', 5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = input("=> ")
    while message != 'q':
        s.sendto(message.encode("utf-8"), server)
        data, addr = s.recvfrom(4028)
        print('Reply: ' + str(data.decode("utf-8")))
        message = input("=> ")
    s.close()


if __name__ == '__main__':
    Main()
