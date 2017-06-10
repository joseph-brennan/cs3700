import os
import socket
import threading


class Server:
    def __init__(self):
        self.serverPort = 5010
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connection(self):

        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.socket.bind(('', self.serverPort))

        self.socket.listen(5)

        print("The server is ready to receive")

        while True:

            connection_socket, address = self.socket.accept()

            threading.Thread(self.loop(connection_socket, address)).start()

    def loop(self, connection_socket, addresss):

        str_header = connection_socket.recv(4096)

        header = str_header.split('\n')
        if header[0] == "Get":
            print header[0]

            if os.path.isfile(header[1]):
                print header[1]

                f = open(header[1], 'rb')

                while True:
                    line = f.read(1048)

                    while line:
                        connection_socket.send(line)
                        print line

                        if f:
                            f.close()
                            self.socket.close()

            else:
                print("404 Not Found")
                connection_socket.send("404 Not Found")
                connection_socket.close()
        else:
            print("400 Bad Request")
            connection_socket.send("400 Bad Request")
            connection_socket.close()


if __name__ == '__main__':
    server1 = Server()
    server1.connection()

