from socket import *


class Server:
    def __init__(self):
        self.serverPort = 5010

    def connection(self):

        server_socket = socket(AF_INET, SOCK_STREAM)

        server_socket.bind(('', self.serverPort))

        server_socket.listen(1)

        print("The server is ready to receive")

        self.loop(server_socket)

    def loop(self, server_socket):

        while True:
            connection_socket, addr = server_socket.accept()

            sentence = connection_socket.recv(4096)

            capitalized_sentence = sentence.upper()

            connection_socket.send(capitalized_sentence)

        connection_socket.close()

if __name__ == '__main__':
    server1 = Server()
    server1.connection()
