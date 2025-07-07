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




clf = KMeans(n_clusters=5)
# mo?emy u?y? metod fit(), predict()
clf.fit(X)
y_pred = clf.predict(X)
# albo metody fit)predict, która ??czy dwie powy?sze
y_pred = clf.fit_predict(X)
