from socket import *
serverName = 'localhost'
serverPort = 6000
clientSocket = socket(AF_INET,SOCK_DGRAM)
while True:
 sentence = input("Input a lowercase sentence: ")
 if sentence == "Quit":
   break
 clientSocket.sendto(sentence.encode(), (serverName, serverPort))
 modifiedsentence, serverAddress = clientSocket.recvfrom(2048)
 print(modifiedsentence.decode())
clientSocket.close()