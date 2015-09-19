import matplotlib.pyplot as plt
from random import random
from math import log, sqrt
from sys import argv


# constructs a historgram from a flattened list
def hist(x, xlab="Number", title="Histogram", ylab = 'Frequency'):
    plt.hist(x, bins=25, color='blue')
    plt.ylabel(ylab)
    plt.xlabel(xlab)
    plt.title(title)
    plt.show()


def coin_flip(p = 0.5):
    if random() < p:
        return 1.0
    else:
        return 0.0

# 412% faster when n = 1000
# could also write as sum(coinflip() / denominator
def uniform(n = 30):
    denominator = 2
    sum = 0.0
    for i in range(n):
        sum += (coin_flip() / denominator)
        denominator <<= 1
    return sum

#http://en.wikipedia.org/wiki/Binary_logarithm
def exponential(lmbda = 2):
    y = uniform()
    return -lmbda * log(1 - y)

#http://en.wikipedia.org/wiki/Marsaglia_polar_method
#http://www.taygeta.com/random/gaussian.html
def gaussian(mean = 0, stdDev = 1):
    d = 1.0
    while (d >= 1.0 or d == 0):
        x = uniform() * 2 - 1
        y = uniform() * 2 - 1
        d = x * x + y * y
    d = sqrt( (-2.0 * log(d)) / d )
    return mean + stdDev * d * x


def gaussian_CLT(n):
    x = 0.0
    for _ in range(n):
        x += exponential()

    return x

def mean(array):
    return sum(array) / float(len(array))

def std_dev(array):
    n = float(len(array))
    mu = mean(array)
    ss = 0
    for x in array:
        ss += ((x - mu) * (x - mu))
    return sqrt(ss / n)

def normalize(array):
    mu = mean(array)
    sigma = std_dev(array)

    for i in range(len(array)):
        array[i] = (array[i] - mu) / sigma

    return array


N = int(argv[1])

data = []
for _ in range(N):
    data.append(gaussian_CLT(100))

hist(normalize(data))