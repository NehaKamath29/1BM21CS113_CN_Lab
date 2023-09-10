from socket import *
serverPort=12000
serverName="127.0.0.1"
clientSocket=socket(AF_INET,SOCK_DGRAM)
sentence=input("Enter file name:\n")
clientSocket.sendto(bytes(sentence,"utf-8"),(serverName,serverPort))
filecontents, serverAddress=clientSocket.recvfrom(2048)
print("Reply from server:\n")
print(filecontents.decode("utf-8"))
clientSocket.close()
clientSocket.close()