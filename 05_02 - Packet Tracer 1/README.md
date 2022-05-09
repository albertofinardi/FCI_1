# Comandi Cisco Packet Tracer

## Permessi utente ( Hostname> ):
| Comando | Utilizzo |
| ------ | ------ |
| ``` ping``` | pinga connessione IP |
| ``` traceroute``` | pinga tutti i nodi intermedi in una connessione |
| ``` enable``` | permessi privilegiati (da Hostname> diventa Hostname#) 

## Permessi Privilegiati ( Hostname# ):
| Comando | Utilizzo |
| ------ | ------ |
| ``` show running-config``` | mostra configurazione corrente |
| ``` show startup-config``` | mostra configurazione al riavvio |
| ``` copy running-config startup-config``` | salva le configurazioni impostate |
| ``` conf t``` | terminale configurazione |
| ``` reload``` | riavvia server |
| ``` disable``` | esci da permessi privilegiati ( da Hostname# a Hostname> ) |
| ``` show ip route``` | visualizza tabella routing |

## Terminale Configurazione ( Hostname(config)# ):
| Comando | Utilizzo |
| ------ | ------ |
| ``` hostname <name>``` | cambio nome hostname |
| ``` enable secret <psw>``` | imposta password per accesso permessi privilegiati |
| ``` no enable secret``` | rimuove password |
| ``` exit``` | esce da modalitˆ configurazione |
| ``` interface <name>``` | modalitˆ configurazione interfaccia specifica |

## Terminale Configurazione Interfaccia ( Hostname(config-if)# ):
| Comando | Utilizzo |
| ------ | ------ |
| ``` IP address <ip> <netmask>``` | configurazione ip|
| ``` no shutdown``` | accendere interfaccia |
| ``` clock rate <rate>``` | impostare clock in |
| ``` description <descr>``` | descrizione router |
| ``` arp timeout <time>``` | modifica timeout di interfaccia |
Seriali non utilizzano ARP


## Su PC ( command terminal ):
| Comando | Utilizzo |
| ------ | ------ |
| ``` telnet <ip> ``` | accesso a router via internet |
| ``` ping <ip> ``` | pinga router |