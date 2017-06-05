from socket import *

serverPort = 5010

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind('', serverPort)

print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(4096)
    modifiedMessage = message.decode()
    serverSocket.sendto(modifiedMessage.endcode(), clientAddress)
