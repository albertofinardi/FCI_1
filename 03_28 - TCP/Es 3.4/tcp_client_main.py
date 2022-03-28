from socket import socket, AF_INET, SOCK_STREAM
import time


def main():
    serverName = 'localhost'
    serverPort = 12000

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    message = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean m'
    # Messaggio 100 caratteri
    for c in message:
        clientSocket.send(c.encode('utf-8'))
        time.sleep(1) # Riga aggiunta per seconda parte esercizio
    clientSocket.send('.'.encode('utf-8')) # Carattere terminatore
    clientSocket.close()


if __name__ == '__main__':
    main()
