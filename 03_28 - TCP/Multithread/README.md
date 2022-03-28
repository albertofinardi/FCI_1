# Multithreaded servers
Per gestire client multipli il server deve attivare più workers:
- un worker per gestire le richieste di connessione entranti
(listening o Welcome worker)
- un worker per gestire ciascuna connessione (active worker)
### Tre paradigmi:
1. ogni worker è un thread
   - facile e veloce 
   - alcune limitazioni (numero max di thread paralleli, tutti i thread hanno gli stessi permessi etc...)
2. ogni worker è un processo 
   - aggiunge complessità e latenza
3. un solo worker che serve a turno un messaggio da ogni socket (molto efficiente, ma più complicato da gestire).
