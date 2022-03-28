from socket import socket, AF_INET, SOCK_STREAM


def main():
    serverPort = 12000

    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    print('Server in ascolto')
    while True:
        clientSocket, clientAddress = serverSocket.accept()
        print(f'Connessione {clientAddress}')
        while True: # Connessione persistente (sennò Pipe error con sleep time)
            message = clientSocket.recv(2048).decode('utf-8')
            print(f'Numero caratteri: {len(message)}')
            if message == '.':
                break
        clientSocket.close()
        print(f'Connessione {clientAddress} chiusa')


if __name__ == '__main__':
    main()
