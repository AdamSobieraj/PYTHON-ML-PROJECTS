from sklearn.cluster import MiniBatchKMeans

import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
# ?rodki naszych klastrów
centroids = np.array([
                        [ 0.8, 2.0],
                        [-0.5, 2.0],
                        [-2.0, 2.0],
                        [-2.5, 2.5],
                        [-2.5, 1.0]
                        ])
# wprowadzenie szumu do naszych klastrów, aby rozrzuci? próbki
blob_std = np.array([0.4, 0.3, 0.1, 0.1, 0.1])
# stworzenie zbioru danych
X, y = make_blobs(
n_samples=3000,
centers=centroids,
cluster_std=blob_std,
random_state=7
)


# %timeit
# metoda MiniBatchKMeans
MBKMeans_clf = MiniBatchKMeans(n_clusters=5, max_iter=10,
random_state=1)
MBKMeans_clf.fit(X)
# 1 loop, best of 3: **11.8 s per loop**


from sklearn.cluster import KMeans
# %timeit
# metoda KMeans
KMeans_clf = KMeans(n_clusters=5, max_iter=10, random_state=1)
KMeans_clf.fit(X)
# 1 loop, best of 3: **15.9 s per loop**