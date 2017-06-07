import socket


class Server:
    def __init__(self):
        self.serverPort = 5010
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connection(self):

        # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket.bind(('', self.serverPort))

        self.socket.listen(1)

        print("The server is ready to receive")

    def loop(self):

        while True:
            connection_socket, addr = self.socket.accept()

            sentence = connection_socket.recv(4096)

            capitalized_sentence = sentence.upper()

            connection_socket.send(capitalized_sentence)

            connection_socket.close()

if __name__ == '__main__':
    server1 = Server()
    server1.connection()
    server1.loop()
