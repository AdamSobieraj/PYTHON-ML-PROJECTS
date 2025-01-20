import numpy as np
from matplotlib import pyplot as plt
from scipy import stats


def gauss(x, sigma=1, mu=0):
    return stats.norm.pdf(x, mu, sigma)
x = np.linspace(-10, 10, 10000)
plt.figure(figsize=(12, 8))
plt.plot(x, gauss(x, sigma=1), label='odchylenie standardowe = 1, średnia = 0')
plt.plot(x, gauss(x, sigma=2), label='odchylenie standardowe = 2, średnia = 0')
plt.plot(x, gauss(x, sigma=5), label='odchylenie standardowe = 5, średnia = 0')
plt.plot(x, gauss(x, sigma=10), label='odchylenie standardowe = 10, średnia = 0')
plt.legend(loc='upper left')
plt.show()