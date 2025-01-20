from matplotlib import pyplot as plt
from scipy import stats

p = 0.1
n = 100
bern_func = stats.bernoulli.rvs(p, size=n)
print(bern_func)
bern_probability = [bern_func[bern_func==0].shape[0]/bern_func.shape[0],
                    bern_func[bern_func==1].shape[0]/bern_func.shape[0]]
plt.scatter([0, 1], bern_probability, color='red')
plt.vlines([0, 1], 0, bern_probability, color='red', lw=2, alpha=0.5)
plt.ylim([0, 1])
plt.show()