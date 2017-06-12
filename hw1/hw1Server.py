import os
import socket
from threading import Thread


class Server:
    def __init__(self):
        self.serverPort = 5010
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connection(self):

        # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket.bind(('', self.serverPort))

        self.socket.listen(5)

        print("The server is ready to receive")

    def loop(self):
        connection_socket, address = self.socket.accept()

        str_header = connection_socket.recv(4096)

        header = str_header.split('\n')
        if header[0] == "Get":
            print header[0]

            if os.path.isfile(header[1]):

                read_file = open(header[1], 'r')

                connection_socket.send(read_file)

            else:
                print("404 Not Found")
                connection_socket.send("404 Not Found")
        else:
            print("400 Bad Request")
            connection_socket("400 Bad Request")

        connection_socket.close()


if __name__ == '__main__':
    server1 = Server()
    server1.connection()
    server1.loop()
