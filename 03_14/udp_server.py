# WHILE -> server rimane attivo sempre (in ascolto del client)
#clientAddress -> tupla con IP e porta

from socket import socket, AF_INET, SOCK_DGRAM


def main():
    serverPort = 12000

    serverSocket = socket(AF_INET, SOCK_DGRAM)  # AF_NET -> ipv4
    # AF_NET6 -> ipv6
    # SOCK_DGRAM -> UDP (DGRAM = datagrammi)
    # SOCK_STREAM -> TCP (STREAM = flusso tcp)

    serverSocket.bind(('', serverPort))
    print('Server attivo')

    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        # 2048 = dimensione buffer di ricezione -> deve essere >= del contenuto trasmesso (sennò informazione persa)

        message = message.decode('utf-8')
        modifiedMessage = message.upper()

        serverSocket.sendto(modifiedMessage.encode('utf-8'), clientAddress)



if __name__ == '__main__':
    main()