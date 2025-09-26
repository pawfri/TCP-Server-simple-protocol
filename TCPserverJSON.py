from socket import *
import threading
import random
import json

# Service
def service(connectionSocket):
    welcomeMessage = 'Insert JSON of format: {"method": "command", "number1": x, "number2": y}. Type exit to disconnect.'
    connectionSocket.send(welcomeMessage.encode())

    while True:
        message = connectionSocket.recv(1024).decode().lower().strip()

        if message == 'exit':
            connectionSocket.send("You have disconnected".encode())
            connectionSocket.close()
            break

        # Parse the JSON-formatted message and extract the command and numeric values
        data = json.loads(message)
        command = data.get("method", "").lower()
        number1 = data.get("number1")
        number2 = data.get("number2")

        
        if command == 'add':
            result = number1 + number2

            connectionSocket.send(str(result).encode())

        elif command == 'subtract':
            result = number1 - number2

            connectionSocket.send(str(result).encode())
            
        elif command == 'random':
            result = random.randint(number1, number2)

            connectionSocket.send(str(result).encode())

        else:
            connectionSocket.send('Error. Must be JSON format: {"method": "command", "number1": X, "number2": Y}'.encode())


# Concurrent Server
serverport = 21
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverport))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=service, args=(connectionSocket,)).start()