from socket import socket, AF_INET, SOCK_DGRAM

def main():
    serverPort = 12000
    vocali = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    serverSocket = socket(AF_INET, SOCK_DGRAM)  # AF_NET -> ipv4
    # AF_NET6 -> ipv6
    # SOCK_DGRAM -> UDP (DGRAM = datagrammi)
    # SOCK_STREAM -> TCP (STREAM = flusso tcp)

    serverSocket.bind(('', serverPort))
    print(f'Server attivo, porta {serverPort}')

    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        # 2048 = dimensione buffer di ricezione -> deve essere >= del contenuto trasmesso (sennò informazione persa)
        print(f'Connessione: {clientAddress[0]}:{clientAddress[1]}')
        message = message.decode('utf-8')
        consonanti = 0

        for c in message:
            if c not in vocali:
                consonanti += 1

        serverSocket.sendto(str(consonanti).encode('utf-8'), clientAddress)



if __name__ == '__main__':
    main()