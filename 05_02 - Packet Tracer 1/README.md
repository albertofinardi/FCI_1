# Comandi Cisco Packet Tracer

## Permessi utente -> Hostname> :

```console ping``` -> pinga connessione IP
```console traceroute``` -> pinga tutti i nodi intermedi in una connessione
```console enable``` -> permessi privilegiati (da Hostname> diventa Hostname#)


## Permessi Privilegiati -> Hostname# :
```console show running-config``` -> configurazione corrente
```console show startup-config``` -> configurazione al riavvio
```console copy running-config startup-config``` -> salva le configurazioni impostate
```console conf t``` -> terminale configurazione
```console reload``` -> riavvia server
```console disable``` -> esci da permessi privilegiati
```console show ip route``` -> visualizza tabella routing

## Terminale Configurazione -> Hostname(config)# :
```console hostname <name>``` -> cambio hostname
```console enable secret <psw>``` -> x diventa password per accesso permessi privilegiati
```console no enable secret``` -> rimuove password
```console exit``` -> esce da modalitˆ configurazione
```console interface <name>``` -> configurazione interfaccia specifica

## Terminale Configurazione Specifica -> Hostname(config-if)# :
```console IP address <ip> <netmask>``` -> configurazione ip
```console no shutdown``` -> accendere interfaccia 
```console clock rate <rate>``` -> impostare clock in 
```console description <descr>``` -> descrizione router
```console arp timeout <time>``` -> modifica timeout di interfaccia


Seriali non utilizzano ARP


Su PC
telnet ip -> accesso a router via internet






