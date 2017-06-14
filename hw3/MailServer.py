import socket
import threading


class MailServer:
    def __init__(self):
        self.serverPort = 5010

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.hostname = socket.gethostbyname(socket.gethostname())

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

            split = client_hello.split()

            if split[0] == "Helo":
                server_hello = "250 %s Hello " % self.hostname + address[0]

                connection_socket.send(server_hello)

                self.from_call(connection_socket)

                self.to_call(connection_socket)

                self.data_call(connection_socket)

                self.mail_call(connection_socket)

            elif client_hello == "QUIT":
                connection_socket.send("221 <%s> closing connection" % address[0])
                break

            else:
                connection_socket.send("503 5.5.2 Send hello first")

        connection_socket.close()

    def from_call(self, connection_socket):
        while True:

            client_from = connection_socket.recv(1024)

            split = client_from.split()

            if split[0].upper() + " " + split[1].upper() == "MAIL FROM":
                connection_socket.send("250 2.1.0 Sender OK")

                return

            else:
                connection_socket.send("03 5.5.2 Need mail command")

    def to_call(self, connection_socket):
        while True:
            client_to = connection_socket.recv(1024)

            split = client_to.split()

            if split[0].upper() + " " + split[1].upper() == "RCPT TO":
                connection_socket.send("250 2.1.5 Recipient OK")

                return

            else:
                connection_socket.send("03 5.5.2 Need rcpt command")

    def data_call(self, connection_socket):
        while True:
            client_data = connection_socket.recv(1024)

            split = client_data.split()

            if split[0].upper() == "DATA":
                connection_socket.send("354 Start mail input; end with <CRLF>.<CRLF>")

                return

            else:
                connection_socket.send("503 5.5.2 Need data command")

    def mail_call(self, connection_socket):
        email = []
        while True:
            client_email = connection_socket.recv(1024)

            if client_email == ".":

                connection_socket.send("250 Message received and to be delivered")

                mes = '\n'.join(email)

                return

            else:
                email.append(client_email)

                connection_socket.send("continue")

if __name__ == '__main__':
    server1 = MailServer()

    server1.connection()
