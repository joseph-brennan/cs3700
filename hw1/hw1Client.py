import socket
import time


class Client:
    def __init__(self):
        self.server_name = raw_input(' Input the DNS name/ip of your HTTP server: ')
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

        str_header = '\n'.join(header)

        self.timer = time.time()

        self.socket.send(str_header)

        with open(header[1], 'w') as f:
            # print "created and open"

            # print "getting lines"

            line = self.socket.recv(1024)

            time_elapsed = time.time()

            print "the RTT is: %0.3f ms" % ((time_elapsed - self.timer) * 1000.0)

            if line == "400 Bad Request":

                print("400 Bad Request. Get is the only supported method")

                f.close()

            elif line == "404 Not Found":

                print("404 File Not Found")

                f.close()

            print "{0}/{1} HTTP/{2}\nHost: {3}\nUser-Agent: {4}".format(header[0], header[1], header[2],
                                                                        self.server_name, header[3])

            for l in line:

                # print "current line: " + l

                if l.count('\n') == 1:

                    self.counter += 1

                    # print "count: %d" % self.counter

                if self.counter == 4:

                    f.write(line)

                    f.close()

                    self.socket.close()

                    # print "file closed"

                    break
        # self.go_again()
'''
    def go_again(self):
        answer = raw_input("would you like continue? y/N: ")

        if answer is "Y" or "y":
            self.four_line()

        elif answer is "N" or "n":
            self.socket.close()

            # self.socket.send("NULL")

            exit()

        else:
            "invalid response."

            self.go_again()
'''

if __name__ == '__main__':
    client1 = Client()
    client1.connection()
