import socket


class Client:

    def __init__(self):
        self.server_name = '127.0.0.1'  # raw_input(' Input the DNS name/ip of your HTTP server: ')
        self.server_port = 5010
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connection(self):
        try:
            # client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            self.socket.connect((self.server_name, self.server_port))

        except socket.error as mes:
            print "Connection error: %s" % mes

    def four_line(self):
        while True:
            sentence = raw_input('Input lowercase sentence: ')

            self.socket.send(sentence)

            modified_message = self.socket.recv(4096)

            if modified_message == '/n':
                self.socket.close()
            else:
                print("From server: " + modified_message)


if __name__ == '__main__':
    client1 = Client()
    client1.connection()
    client1.four_line()
