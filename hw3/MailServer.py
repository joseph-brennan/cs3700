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
        while True:
            client_hello = connection_socket.recv(1024)

            if client_hello == "Helo":
                server_hello = client_hello + " " + address[0]

                connection_socket.send(server_hello)

                self.from_call(connection_socket, address)

            elif client_hello == "NULL":
                break

            else:
                connection_socket.send("503 5.5.2 Send hello first")

        connection_socket.close()

    def from_call(self, connection_socket, address):
        while True:

            client_from = connection_socket.recv(1024)

            server_from = client_from

            if client_from.upper() == "MAIL FROM":
                connection_socket.send(server_from)

                self.to_call(connection_socket, address)
            else:
                connection_socket.send("03 5.5.2 Need mail command")

    def to_call(self, connection_socket, address):
        while True:
            client_to = connection_socket.recv(1024)

            server_to = client_to

            if client_to.upper() == "MAIL TO":
                connection_socket.send(server_to)

                self.data_call(connection_socket, address)

            else:
                connection_socket.send("03 5.5.2 Need rcpt command")

    def data_call(self, connection_socket, address):
        while True:
            client_data = connection_socket.recv(1024)

            server_data = client_data

            if client_data.upper() == "DATA":
                connection_socket.send(server_data)
                self.email_server(connection_socket, address)
            else:
                connection_socket.send("503 5.5.2 Need data command")


if __name__ == '__main__':
    server1 = MailServer()

    server1.connection()
