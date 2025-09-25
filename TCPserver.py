from socket import *
import threading

# Service
def service(connectionSocket):
    message = connectionSocket.recv(1024).decode()
    #TODO add service logic

# Concurrent Server
serverport = 21
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverport))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=service, args=(connectionSocket)).start()