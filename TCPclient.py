from socket import *

# CLIENT
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('localhost', 21))

welcome = clientSocket.recv(1024).decode()
print(f'{welcome}')

while True:
    request = input('Enter request:')
    clientSocket.send(request.encode())
    response = clientSocket.recv(1024).decode()
    print(f'Response from server: {response}')
    if request.lower() == 'exit':
        print('Exiting client.')
        break
clientSocket.close()