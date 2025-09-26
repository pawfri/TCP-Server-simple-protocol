from socket import *
import threading
import random
import json

# Service
def service(connectionSocket):
    # Welcome message explaining server functionality to the client when connecting
    welcomeMessage = 'Insert JSON of format: {"method": "command", "number1": x, "number2": y}. Type exit to disconnect.'
    connectionSocket.send(welcomeMessage.encode())

    while True:
        message = connectionSocket.recv(1024).decode().lower().strip()

        # Handling client request to disconnect from the server
        if message == 'exit':
            connectionSocket.send("You have disconnected".encode())
            connectionSocket.close()
            break

        try:
            # Parse the JSON-formatted message and extract the command and numeric values
            data = json.loads(message)
            command = data.get("method", "").lower()
            number1 = data.get("number1")
            number2 = data.get("number2")
            
            # Handling addition of two numbers
            if command == 'add':
                result = number1 + number2

                connectionSocket.send(str(result).encode())

            # Handling subtraction of two numbers
            elif command == 'subtract':
                result = number1 - number2

                connectionSocket.send(str(result).encode())
            
            # Handling a random number between two numbers, both included
            elif command == 'random':
                result = random.randint(number1, number2)

                connectionSocket.send(str(result).encode())

            # Handling of unknown commands
            else:
                connectionSocket.send('Error: Unkown command. Use add, subtract or random'.encode())
            
        # Handling of cases where JSON format is not used
        except json.JSONDecodeError:
            connectionSocket.send('Error: Must be JSON format: {"method": "command", "number1": X, "number2": Y}'.encode())


# Concurrent Server
serverport = 1337
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverport))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=service, args=(connectionSocket,)).start()