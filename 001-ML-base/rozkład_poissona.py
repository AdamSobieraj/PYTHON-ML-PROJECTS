import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

poisson_set = stats.poisson.rvs(mu=10, size=10000)

plt.hist(poisson_set, density=True, edgecolor='black', bins=28)
plt.show()

print('Prawdopodobieństwo, że w następnych 15 minutach będzie 5 połączeń:')
print(np.round(1 - stats.poisson.cdf(k=5, mu=10), 2))