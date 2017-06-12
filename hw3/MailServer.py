import socket
import threading


class MailServer:
    def __init__(self):
        self.serverPort = 5010

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def connection(self):

        self.socket.bind(('', self.serverPort))

        self.socket.listen(5)

        print("The server is ready to receive")

        while True:
            connection_socket, address = self.socket.accept()

            sender = "220"

            connection_socket.send(sender)

            threading.Thread(self.email_server(connection_socket, address)).start()

    def email_server(self, connection_socket, address):
        client_hello = connection_socket.recv(1024)

        if client_hello == "Helo":
            server_hello = client_hello + address[0]

            connection_socket.send(server_hello)

        else:

            connection_socket.send("503 5.5.2 Send hello first")

        client_from = connection_socket.recv(1024)

        server_from = client_from

        connection_socket.send(server_from)

        client_to = connection_socket.recv(1024)

        server_to = client_to

        connection_socket.send(server_to)

        client_data = connection_socket.recv(1024)

        server_data = client_data

        connection_socket.send(server_data)


if __name__ == '__main__':
    server1 = MailServer()

    server1.connection()

