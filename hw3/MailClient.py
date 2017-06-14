import socket
import time


class MailClient:
    def __init__(self):
        self.server_name = raw_input("Input the DNS name/ip of your HTTP server: ")

        self.server_port = int(raw_input("Input the port number of your connection: "))

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
        f = open("testResultsClient.txt", 'w')

        while True:
            self.client_hello(f)

            self.client_from(f)

            self.client_to(f)

            self.client_data(f)

            self.mail_message()

            running = raw_input("would you like to continue? Y/n: ").strip().lower()

            if running == 'y':
                continue

            if running == 'n':
                break

        self.socket.send("QUIT")

        mes = self.socket.recv(1024)

        print mes

        f.write(mes)

        self.socket.close()

        f.close()

        exit(0)

    def client_hello(self, f):
        while True:
            client_hello = raw_input("Input command and domain name: ")

            self.socket.send(client_hello)

            self.start_hello = time.time()

            server_hello = self.socket.recv(1024)

            self.end_hello = time.time()

            if server_hello == "503 5.5.2 Send hello first":
                print "503 5.5.2 Send hello first"

                continue

            print "the RTT for Hello is: %0.3f ms" % ((self.end_hello - self.start_hello) * 1000.0)

            print server_hello

            f.write(server_hello + '\n')

            return

    def client_from(self, f):
        while True:
            client_from = raw_input("Input the sender's address: ")

            self.socket.send(client_from)

            self.start_from = time.time()

            server_from = self.socket.recv(1024)

            self.end_from = time.time()

            if server_from == "03 5.5.2 Need mail command":
                print "03 5.5.2 Need mail command"

                continue

            print "the RTT for sender is: %0.3f ms" % ((self.end_from - self.start_from) * 1000.0)

            print server_from

            f.write(server_from + '\n')

            return

    def client_to(self, f):
        while True:
            client_to = raw_input("Input the receiver's address: ")

            self.socket.send(client_to)

            self.start_to = time.time()

            server_to = self.socket.recv(1024)

            self.end_to = time.time()

            if server_to == "03 5.5.2 Need rcpt command":
                print "03 5.5.2 Need rcpt command"

                continue

            print "the RTT for receiver is: %0.3f ms" % ((self.end_to - self.start_to) * 1000.0)

            print server_to

            f.write(server_to + '\n')

            return

    def client_data(self, f):
        while True:
            client_data = raw_input("Input the data code: ")

            self.socket.send(client_data)

            self.start_data = time.time()

            server_data = self.socket.recv(1024)

            self.end_data = time.time()

            if server_data == "503 5.5.2 Need data command":
                print "503 5.5.2 Need data command"

                continue

            print "the RTT for data is: %0.3f ms" % ((self.end_data - self.start_data) * 1000.0)

            print server_data

            f.write(server_data + '\n')

            return

    def mail_message(self):
        while True:
            line = raw_input(">>> ")

            self.socket.send(line)

            check = self.socket.recv(1024)

            if check == "250 Message received and to be delivered":
                print check

                return

            elif check == "continue":
                continue
'''        
        lines = []

        while True:
            line = raw_input(">>> ")

            if line == ".":
                break

            else:
                lines.append(line)

        email = '\n'.join(lines)

        print email
#########################################
        lines = sys.stdin.readlines()

        for i in range(len(lines)):
            if lines[i] == ".\n":
                print "win win"

        print lines

    def ouput(self, server_hello, server_from, server_to, server_data):

        print server_hello

        print "the RTT for Hello is: %0.3f ms" % ((self.end_hello - self.start_hello) * 1000.0)

        print server_from

        print "the RTT for sender is: %0.3f ms" % ((self.end_from - self.start_from) * 1000.0)

        print server_to

        print "the RTT for receiver is: %0.3f ms" % ((self.end_to - self.start_to) * 1000.0)

        print "the RTT for data is: %0.3f ms" % ((self.end_data - self.start_data) * 1000.0)

        print server_data

        return
'''


if __name__ == '__main__':
    client1 = MailClient()

    client1.connection()
