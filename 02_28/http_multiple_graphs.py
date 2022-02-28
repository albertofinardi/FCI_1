import requests
import matplotlib.pyplot as plt

urls = ['http://www.google.com', 'http://www.netflix.com', 'http://www.polimi.it']


def elapsed_plot(num_iter):
    for url in urls:
        times = []
        for it in range(num_iter):
            r = requests.get(url)
            times.append(r.elapsed.microseconds/1000)
        plt.plot(times, label=f'{url}')


    plt.ylabel('Ritardo end-to-end (ms)')
    plt.xlabel('Iterazione')
    plt.title(f'GET requests')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    elapsed_plot(10)
