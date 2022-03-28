import requests
import matplotlib.pyplot as plt
url = 'http://www.google.com'


def elapsed_plot(num_iter):
    times = []
    for i in range(num_iter):
        r = requests.get(url)
        times.append(r.elapsed.microseconds/1000)

    plt.plot(times)
    #plt.hist(times)
    plt.hlines(max(times), 0, num_iter, colors='red')
    plt.hlines(min(times), 0, num_iter, colors='red')
    plt.ylabel('Ritardo end-to-end (ms)')
    plt.xlabel('Iterazione')
    plt.title(f'GET request {url}')
    plt.grid()
    plt.show()


def elapsed_boxplot(num_iter):
    times = []
    for i in range(num_iter):
        r = requests.get(url)
        times.append(r.elapsed.microseconds/1000)

    plt.boxplot(times)
    plt.ylabel('Ritardo end-to-end (ms)')
    plt.title(f'GET request {url}')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    elapsed_plot(10)
    #elapsed_boxplot(10)
