import requests
url = 'http://www.google.com'


def elapsed_single():
    r = requests.get(url)
    print(f'\nRitardo: {r.elapsed.microseconds / 1000} ms')
    # Tempo di round trip in millisecondi, ossia host -> server e ritorno (server -> host) [ritardo end to end].
    # Docs: [https: // docs.python - requests.org / en / latest / api / requests.Response]
    # Ping (uguale, ma al posto di indirizzo web usi indirizzo IP) è rispetto a layer 3, mentre elapsed è rispetto a
    # tutto il processo.
    # Tempo lettura (parsing + travel) header di ritorno - tempo partenza PDU.
    # Ritardo su internet è al più nell'ordine centinaia di millisecondi -> se è maggiore ci sono problemi.


def elapsed_mean_max_min(num_iter):
    print(f'\nIterazioni: {num_iter}')
    times = []
    for i in range(num_iter):
        r = requests.get(url)
        times.append(r.elapsed.microseconds/1000)
    print(f'Tempi round-trip: {times}')
    max_time = max(times)
    min_time = min(times)
    mean_time = sum(times) / len(times)

    # Per calcolare la media:
    # -> sum/len
    # -> statistics.mean()
    # -> numpy.mean() [installa numpy]

    print(f'\nRitardo max: {max_time} ms')
    print(f'Ritardo min: {min_time} ms')
    print(f'Ritardo medio: {mean_time} ms')


def content_url():
    r = requests.get(url)
    print(f'\nStatus code: {r.status_code}')
    print(f'Content: {r.text}')


if __name__ == '__main__':
    print(f'\nURL: {url}')
    # Commenta la funzione (o più) che non vuoi utilizzzare con '#'
    # elapsed_single()
    # elapsed_mean_max_min(10)
    content_url()
