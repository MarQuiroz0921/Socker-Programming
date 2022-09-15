from socket import *
serverName = 'localhost'
serverPort = 5555
while True:
    sentence = input("Input a lowercase sentence please: ")
    if sentence =="Quit":
      break
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print(modifiedSentence.decode())
    clientSocket.close()


