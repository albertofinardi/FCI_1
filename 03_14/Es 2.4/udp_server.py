from socket import socket, AF_INET, SOCK_DGRAM

def main():
    serverPort = 12500

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
        k = int(message)
        response = ''

        if k > 1:
            for i in range(2, int(k / 2) + 1):
                if (k % i) == 0:
                    response = 'Numero non primo'
                    break
            else:
                response = 'Numero primo'
        else:
            response = 'Numero non primo'

        serverSocket.sendto(response.encode('utf-8'), clientAddress)



if __name__ == '__main__':
    main()