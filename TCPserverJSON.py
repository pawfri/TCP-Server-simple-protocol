from socket import *
import threading
import random
import json

# Service
def service(connectionSocket):
    welcomeMessage = 'To start insert JSON of format: {"method": "command", "numberX": X, "numberY": Y}. Type exit to disconnect.'
    connectionSocket.send(welcomeMessage.encode())

    while True:
        message = connectionSocket.recv(1024).decode().lower().strip()

        if message == 'exit':
            connectionSocket.send("You have disconnected".encode())
            connectionSocket.close()
            break

        
        # if message == 'add':
            # TODO: Implement logic

        # elif message == 'subtract':
            # TODO: Implement logic
            
        # elif message == 'random':
            # TODO: Implement logic

        else:
            connectionSocket.send("Unknown command. Try: add, subtract or random. Type exit to disconnect".encode())  


# Concurrent Server
serverport = 21
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverport))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=service, args=(connectionSocket,)).start()