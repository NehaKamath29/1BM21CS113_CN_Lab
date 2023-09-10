from socket import *
serverName="127.0.0.1"
serverPort=12000
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence=input("Enter the file name:\n")

clientSocket.send(sentence.encode())

filecontents=clientSocket.recv(1024).decode()

print("Reply from server:\n")
print(filecontents)
clientSocket.close()





'''from socket import *
serverName='127.0.0.1'
serverPort=12000
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence=input("\nEnter file name: ")

clientSocket.send(sentence.encode())
filecontents=clientSocket.recv(1024).decode()
print('\nFrom Server:\n')
print(filecontents)
clientSocket.close()'''