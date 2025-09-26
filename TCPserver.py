from socket import *
import threading
import random

# Service
def service(connectionSocket):
    # Welcome message explaining server functionality to the client when connecting
    welcomeMessage = "To start type: add, subtract or random. To disconnect type: exit."
    connectionSocket.send(welcomeMessage.encode())

    while True:
        message = connectionSocket.recv(1024).decode().lower().strip()

        # Handling client request to disconnect from the server
        if message == 'exit':
            connectionSocket.send("You have disconnected".encode())
            connectionSocket.close()
            break
        
        # Handling addition of two numbers
        elif message == 'add':
            instructionsMessage = "Input numbers. Example: 2 4"
            connectionSocket.send(instructionsMessage.encode())

            calculatorParts = connectionSocket.recv(1024).decode().strip().split()
            x = int(calculatorParts[0])
            y = int(calculatorParts[1])
            result = x + y

            connectionSocket.send(str(result).encode())

        # Handling subtraction of two numbers
        elif message == 'subtract':
            instructionsMessage = "Input numbers. Example: 1 10"
            connectionSocket.send(instructionsMessage.encode())

            calculatorParts = connectionSocket.recv(1024).decode().strip().split()
            x = int(calculatorParts[0])
            y = int(calculatorParts[1])
            result = x - y

            connectionSocket.send(str(result).encode())

        # Handling a random number between two numbers, both included         
        elif message == 'random':
            instructionsMessage = "Input numbers. Example: 2 5"
            connectionSocket.send(instructionsMessage.encode())

            calculatorParts = connectionSocket.recv(1024).decode().strip().split()
            x = int(calculatorParts[0])
            y = int(calculatorParts[1])
            result = random.randint(x, y)

            connectionSocket.send(str(result).encode())

        # Handling of unknown commands
        else:
            connectionSocket.send("Unknown command. Try: add, subtract or random. Type exit to disconnect".encode())  


# Concurrent Server
serverport = 1337
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverport))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=service, args=(connectionSocket,)).start()