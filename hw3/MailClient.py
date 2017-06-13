# import smtplib
import socket
import time


class MailClient:
    def __init__(self):
        self.server_name = "127.0.0.1"  # raw_input("Input the DNS name/ip of your HTTP server: ")

        self.server_port = 5010  # raw_input("Input the port number of your connection: ")

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.start_hello, self.end_hello, self.start_from, self.end_from = 0, 0, 0, 0

        self.start_to, self.end_to, self.start_data, self.end_data = 0, 0, 0, 0

    def connection(self):
        try:
            self.socket.connect((self.server_name, self.server_port))

            print self.socket.recv(1024)

            self.email_client()

        except socket.error as mes:

            print "Connection error: %s" % mes

    def email_client(self):
        while True:
            server_hello = self.client_hello()

            server_from = self.client_from()

            server_to = self.client_to()

            server_data = self.client_data()

            self.ouput(server_hello, server_from, server_to, server_data)

            running = raw_input("would you like to continue? Y/n: ").strip().lower()

            if running == 'y':
                continue

            if running == 'n':
                break

        self.socket.send("NULL")

        self.socket.close()

        exit(0)

    def client_hello(self):
        while True:
            client_hello = raw_input("Input command and domain name: ")

            self.socket.send(client_hello)

            self.start_hello = time.time()

            server_hello = self.socket.recv(1024)

            self.end_hello = time.time()

            if server_hello == "503 5.5.2 Send hello first":
                print "503 5.5.2 Send hello first"

                continue

            return server_hello

    def client_from(self):
        while True:
            client_from = raw_input("Input the sender's address: ")

            self.socket.send(client_from)

            self.start_from = time.time()

            server_from = self.socket.recv(1024)

            self.end_from = time.time()

            if server_from == "03 5.5.2 Need mail command":
                print "03 5.5.2 Need mail command"

                continue

            return server_from

    def client_to(self):
        while True:
            client_to = raw_input("Input the receiver's address: ")

            self.socket.send(client_to)

            self.start_to = time.time()

            server_to = self.socket.recv(1024)

            self.end_to = time.time()

            if server_to == "03 5.5.2 Need rcpt command":
                print "03 5.5.2 Need rcpt command"

                continue

            return server_to

    def client_data(self):
        while True:
            client_data = raw_input("Input the data code: ")

            self.socket.send(client_data)

            self.start_data = time.time()

            server_data = self.socket.recv(1024)

            self.end_data = time.time()

            if server_data == "503 5.5.2 Need data command":
                print "503 5.5.2 Need data command"

                continue

            return server_data

    def ouput(self, server_hello, server_from, server_to, server_data):

        print server_hello

        print "the RTT for Hello is: %0.3f ms" % ((self.start_hello - self.end_hello) * 1000.0)

        print server_from

        print "the RTT for sender is: %0.3f ms" % ((self.start_from - self.end_from) * 1000.0)

        print server_to

        print "the RTT for receiver is: %0.3f ms" % ((self.start_to - self.end_to) * 1000.0)

        print server_data

        print "the RTT for email is: %0.3f ms" % ((self.start_data - self.end_data) * 1000.0)

        return


if __name__ == '__main__':
    client1 = MailClient()

    client1.connection()
