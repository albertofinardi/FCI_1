from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
serverPort = 12000


def handler(connectionSocket: socket):
    while True:
        message = connectionSocket.recv(2048).decode('utf-8')
        print(f'[ ] Messaggio ricevuto da {clientAddress}: {message}')
        if message == '.':
            break
        modifiedMessage = message.upper()
        connectionSocket.send(modifiedMessage.encode('utf-8'))
    connectionSocket.close()
    print(f'[-] Chiusura connessione {clientAddress}\n')

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# Necessario per multithread che usano stesso socket, SO_REUSEADDR = 1 (come fosse flag
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('Server in ascolto')

while True:
    newSocket, clientAddress = serverSocket.accept()
    print(f'[+] Connesso con {clientAddress}')
    thread = Thread(target=handler, args=(newSocket,))
    thread.start()