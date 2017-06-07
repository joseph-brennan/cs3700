import socket
import time


class Client:
    def __init__(self):
        self.server_name = '127.0.0.1'  # raw_input(' Input the DNS name/ip of your HTTP server: ')
        self.server_port = 5010
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.timer = time

    def connection(self):
        try:
            self.socket.connect((self.server_name, self.server_port))

        except socket.error as mes:

            print "Connection error: %s" % mes

    def four_line(self):
        while True:
            header = [raw_input("input the HTTP method type: "), raw_input("name of the htm file requested: "),
                      raw_input("HTTP Version: "), raw_input("User Agent: ")]

            str_header = '\n'.join(header)

            self.socket.send(str_header)

            my_file = self.socket.recv(4096)

            print("From server: " + my_file)

if __name__ == '__main__':
    client1 = Client()
    client1.connection()
    client1.four_line()
