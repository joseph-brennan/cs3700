import socket
import time


class Client:
    def __init__(self):
        self.server_name = '127.0.0.1'  # raw_input(' Input the DNS name/ip of your HTTP server: ')
        self.server_port = 5010
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.timer = time
        self.counter = 0

    def connection(self):
        try:
            self.socket.connect((self.server_name, self.server_port))
            self.four_line()
        except socket.error as mes:

            print "Connection error: %s" % mes

    def four_line(self):
        header = [raw_input("input the HTTP method type: "), raw_input("name of the htm file requested: "),
                  raw_input("HTTP Version: "), raw_input("User Agent: ")]

        self.timer = time.clock()
        str_header = '\n'.join(header)

        self.socket.send(str_header)

        with open("whatever 2.txt", 'w+') as f:
            print "created and open"

            print "getting lines"

            time_end = time.time()

            print time_end - self.timer

            while True:
                line = self.socket.recv(4096)
                if line == "400 Bad Request":

                    print("400 Bad Request. Get is the only supported method")

                    f.close()

                    break
                elif line == "404 Not Found":

                    print("404 Not Found")

                    f.close()

                    break

                print "current line: " + line

                while line is '\n':

                    f.close()
                    print "file closed"
                    break
                f.write(line)
        self.socket.close()

        # my_file = self.socket.recv(4096)

        # filling_file = [my_file]
        #
        # print("From server: " + my_file)
        #
        # if my_file == "/n":
        #     self.counter += 1
        #
        # else:
        #     self.counter = 0
        #
        # if self.counter == 4:
        #     this_file = open("whatever 2.txt", 'w+')
        #
        #     for item in filling_file:
        #
        #         this_file.write(item)
        #
        #         this_file.close()
        #
        #         self.socket.close()
        #
        #         break


if __name__ == '__main__':
    client1 = Client()
    client1.connection()
