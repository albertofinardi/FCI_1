import requests

urls = ['http://www.google.com', 'http://www.youtube.com', 'http://www.polimi.it', 'http://www.wikipedia.org', 'http://www.amazon.com', 'http://www.twitter.com']


def media(lista):
    return sum(lista)/len(lista)


def best_mean_fn(iterations):
    means = []
    for (i, url) in enumerate(urls):
        print(f'\n\nElaborazione {url} ({i+1}/{len(urls)})')
        times = []
        for it in range(iterations):
            print(f'Iterazione {it}')
            r = requests.get(url)
            times.append(r.elapsed.microseconds / 1000)
        mean = media(times)
        print(f'Media : {mean} ms')
        means.append(mean)

    best_mean = min(means)
    best_i = means.index(best_mean)
    print(f'\n\nMigliore tempo medio ({urls[best_i]}): {best_mean} ms')


if __name__ == '__main__':
    best_mean_fn(10)
