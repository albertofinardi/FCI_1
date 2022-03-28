import requests
import matplotlib.pyplot as plt

urls = ['http://www.google.com', 'http://www.netflix.com', 'http://www.polimi.it']


def elapsed_plot(num_iter):
    best_mean = 100000
    best_i = -1
    for (i, url) in enumerate(urls):
        times = []
        print(f'Elaborazione {url}')
        for it in range(num_iter):
            print(f'Iterazione: {it}')
            r = requests.get(url)
            times.append(r.elapsed.microseconds/1000)
        # Il ciclo precedente è riassumibile in:
        # times = [requests.get(url).elapsed.microseconds/1000 for _ in range(num_iter)]

        plt.plot(times, label=f'{url}')
        mean = sum(times) / len(times)

        if mean < best_mean:
            best_mean = mean
            best_i = i

    plt.ylabel('Ritardo end-to-end (ms)')
    plt.xlabel('Iterazione')
    plt.title(f'GET requests')
    plt.legend()
    plt.grid()
    plt.show()
    print(f'Migliore tempo medio ({urls[best_i]}): {best_mean} ms')


if __name__ == '__main__':
    elapsed_plot(10)
