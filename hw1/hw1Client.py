from socket import *

serverName = 'hostname'

serverPort = 5010

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = raw_input('Input the DNS name/ip of your HTTP server')

clientSocket.sendto(message.encode(), (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(4096)

print(modifiedMessage.decode())

clientSocket.close()
