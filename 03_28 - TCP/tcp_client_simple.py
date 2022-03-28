from socket import socket, AF_INET, SOCK_STREAM


def main():
    serverName = 'localhost'
    serverPort = 12000

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    message = input('Inserisci messaggio: ')
    clientSocket.send(message.encode('utf-8'))
    # Utilizzi .send al posto di .sendto -> sai già chi è destinatario tramite funzione connect
    # (Stream - connecion oriented)

    modifiedMessage = clientSocket.recv(2048).decode("utf-8")
    #  Utilizzi .recv al posto di .recvfrom

    print(f'Risposta server: {modifiedMessage}')
    clientSocket.close()


if __name__ == '__main__':
    main()
