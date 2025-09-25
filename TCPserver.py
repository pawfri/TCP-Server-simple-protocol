from socket import *
import threading

# Service
def service(connectionSocket):
    welcomeMessage = "To start type: add, subtract or random. To disconnect type: exit."
    connectionSocket.send(welcomeMessage.encode())

    while True:
        message = connectionSocket.recv(1024).decode().strip()
        if not message:
            break

        if message == 'exit':
            connectionSocket.send("You have disconnected".encode())
            connectionSocket.close()
            break

        if message == 'add':
            instructionsMessage = "Send two numbers as: <x> <y> Example: 2 4"
            connectionSocket.send(instructionsMessage.encode())

            calculatorParts = connectionSocket.recv(1024).decode().strip().split()
            x = int(calculatorParts[0])
            y = int(calculatorParts[1])
            result = x + y

            connectionSocket.send(str(result).encode())

        # if message == 'subtract':
            # TODO: add subtract logic
            

        # if message == 'random':
            # TODO: add random logic
            

# Concurrent Server
serverport = 21
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverport))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=service, args=(connectionSocket,)).start()