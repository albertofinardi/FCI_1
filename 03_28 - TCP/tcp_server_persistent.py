from socket import socket, AF_INET, SOCK_STREAM



def main():
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverSocket.bind(('', serverPort))
    # Passive open - ascolto
    # Stringa vuota nella tupla IP significa di rimanere in ascolto su tutti i possibili IP (senza specificarne una)

    serverSocket.listen(1)
    # Lunghezza coda di connessioni host in accesso al server -> mettendo 0 viene impostato un valore default da OS
    # Nel caso un server sia già occupato ed arriva richiesta nuova, o viene rifiutata o viene messa nella
    # coda listen (se c'è posto)

    print('Server in ascolto\n')

    while True:
        connectionSocket, clientAddress = serverSocket.accept()
        # Apertura socket di active open dedicata a quel client -> Three way handshake
        print(f'[+] Connesso con {clientAddress}')

        while True:
            message = connectionSocket.recv(2048).decode('utf-8')
            print(f'\t-> Messaggio ricevuto: {message}')

            if message == '.':
                break
            # Chiusura connessione con carattere terminatore

            modifiedMessage = message.upper()
            # Modifica del messaggio da restituire

            connectionSocket.send(modifiedMessage.encode('utf-8'))
        connectionSocket.close()
        print(f'[-] Chiusura connessione {clientAddress}\n')
        # Chiusura socket specifico a quel client, ma non la passive
        # Se non viene chiusa la connectionSocket, TCP la interpreta come connessione ancora in utilizzo,
        # quindi richieste di altre host vanno in coda listen o rifiutate


if __name__ == '__main__':
    main()
