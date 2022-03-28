from socket import socket, AF_INET, SOCK_DGRAM

def main():
    serverName = 'localhost'
    # localhost = 127.0.0.1
    # Se pc con server su stessa rete locale, usare indirizzo IP del server
    serverPort = 12000

    clientSocket = socket(AF_INET, SOCK_DGRAM)
    # AF_NET -> ipv4
    # AF_NET6 -> ipv6
    # SOCK_DGRAM -> UDP (DGRAM = datagrammi)
    # SOCK_STREAM -> TCP (STREAM = flusso tcp)

    message = input('Inserisci testo: ')
    clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))
    #utf-8 -> tipologia di encoding per trasmissione dati (da stringa a bit)

    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    # 2048 = dimensione buffer di ricezione -> deve essere >= del contenuto trasmesso (sennò informazione persa)

    print(modifiedMessage.decode('utf-8'))

    clientSocket.close()

if __name__ == '__main__':
    main()
