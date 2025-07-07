from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons
# tworzymy zbiór moon
X, y = make_moons(n_samples=1000, noise=0.08)
# tworzymy pierwszy klasyfikator DBSCAN z eps = 0.05
dbscan = DBSCAN(eps=0.05, min_samples=5)
dbscan.fit(X)
# drugi DBSCAN z eps = 0.2 (wi?kszy epsilon, wi?ksza przestrze?wokó?)
dbscan_2 = DBSCAN(eps=0.2, min_samples=5)
dbscan_2.fit(X)