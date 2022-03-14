from socket import socket, AF_INET, SOCK_DGRAM, timeout

def main():
    serverName = 'localhost'
    serverPort = 12000
    timelimit = 2

    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(timelimit) # timeout in secondi (float)

    message = input('Inserisci testo: ')
    clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))

    # try -> codice classico del programma
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(f'Numero consonanti: {modifiedMessage.decode("utf-8")}')

    # except -> se compare un errore (eccezione) in try, blocca il try e passa a codice except
    except timeout:
        print(f'Scaduto timeout di {timelimit} secondi')
    except:
        print('Errore generico')

    # finally -> eseguito sia post try che post except
    finally:
        clientSocket.close()

if __name__ == '__main__':
    main()

