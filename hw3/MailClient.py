# import smtplib
import socket
import time


class MailClient:
    def __init__(self):
        self.server_name = 5010  # raw_input("Input the DNS name/ip of your HTTP server: ")

        self.server_port = '127.0.0.1'  # raw_input("Input the port number of your connection: ")

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connection(self):
        try:
            self.socket.connect((self.server_name, self.server_port))

            print self.socket.recv(1024)

            self.email_client()

        except socket.error as mes:

            print "Connection error: %s" % mes

    def email_client(self):
        while True:
            client_hello = input("Input command and domain name: ")

            self.socket.send(client_hello)

            start_hello = time.time()

            server_hello = self.socket.recv(1024)

            end_hello = time.time()

            if server_hello == "503 5.5.2 Send hello first":
                print "503 5.5.2 Send hello first"

                continue

            client_from = input("Input the sender's address: ")

            self.socket.send(client_from)

            start_from = time.time()

            server_from = self.socket.recv(1024)

            end_from = time.time()

            client_to = input("Input the receiver's address: ")

            self.socket.send(client_to)

            start_to = time.time()

            server_to = self.socket.recv(1024)

            end_to = time.time()

            start_data = time.time()

            end_data = time.time()

            self.ouput(start_hello, server_hello, end_hello, start_from, server_from, end_from, start_to, server_to,
                       end_to, start_data, end_data)

            running = input("would you like to continue? Y/n: ")

            if running == "Y" or "y":
                continue

            elif running == "N" or "n":
                break

        self.socket.close()

    def ouput(self, start_hello, server_hello, end_hello, start_from, server_from, end_from, start_to, server_to,
              end_to, start_data, end_data):

        print server_hello

        print "the RTT for Hello is: %0.3f ms" % ((start_hello - end_hello) * 1000.0)

        print server_from

        print "the RTT for sender is: %0.3f ms" % ((start_from - end_from) * 1000.0)

        print server_to

        print "the RTT for receiver is: %0.3f ms" % ((start_to - end_to) * 1000.0)

        print "the RTT for email is: %0.3f ms" % ((start_data - end_data) * 1000.0)


if __name__ == '__main__':
    client1 = MailClient()

    client1.connection()
