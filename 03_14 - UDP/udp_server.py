# WHILE -> server rimane attivo sempre (in ascolto del client)
# clientAddress -> tupla con IP e porta

from socket import socket, AF_INET, SOCK_DGRAM


def main():
    serverPort = 12000

    serverSocket = socket(AF_INET, SOCK_DGRAM)  # AF_NET -> ipv4
    # AF_NET6 -> ipv6
    # SOCK_DGRAM -> UDP (DGRAM = datagrammi)
    # SOCK_STREAM -> TCP (STREAM = flusso tcp)

    serverSocket.bind(('', serverPort))
    # Lasciando vuota il serverName nella tuple di .bind accetti tutti gli host

    print(f'Server attivo, porta {serverPort}')

    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        # 2048 = dimensione buffer di ricezione -> deve essere >= del contenuto trasmesso (sennò informazione persa)

        message = message.decode('utf-8')
        modifiedMessage = message.upper()
        print(f'Connessione: {clientAddress[0]}:{clientAddress[1]}')

        serverSocket.sendto(modifiedMessage.encode('utf-8'), clientAddress)
        # Non hai nessuna chiusura del socket, sennò server non può accettare altre richieste

if __name__ == '__main__':
    main()
