from socket import *


class Client:

    def __init__(self):
        self.server_name = '127.0.0.1'  # raw_input(' Input the DNS name/ip of your HTTP server: ')
        self.server_port = 5010

    def connection(self):
        try:
            client_socket = socket(AF_INET, SOCK_STREAM)

            client_socket.connect((self.server_name, self.server_port))

            self.four_line(client_socket)

        except:
            print("Input incorrect server name ")

    def four_line(self, client_socket):
        flag = True
        while flag:
            sentence = raw_input('Input lowercase sentence: ')

            client_socket.send(sentence)

            modified_message = client_socket.recv(4096)

            if modified_message == "NULL":
                client_socket.close()
            else:
                print("From server: " + modified_message)


if __name__ == '__main__':
    client1 = Client()
    client1.connection()
