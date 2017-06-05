from socket import *

serverName = raw_input('DNS/IP: ')

serverPort = 5010

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

sentence = raw_input('Input lowercase sentence: ')

clientSocket.send(sentence)

modifiedMessage = clientSocket.recv(4096)

print("From server " + modifiedMessage)

clientSocket.close()
