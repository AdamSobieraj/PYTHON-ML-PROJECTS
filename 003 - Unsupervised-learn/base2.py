import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
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


# tworzymy 19 algorytmów z k od 1 do 19
kmeans_per_k = [KMeans(n_clusters=k, random_state=2).fit(X) for k in range(2, 20) # zaczynamy od warto?ci n_clusters
    # wynosz?cej 2, gdy? nie ma sensu dzielenia zbioru dla 1 klastra
    ]

inertias = [model.inertia_ for model in kmeans_per_k]
plt.plot(range(2, 20), inertias, 'bx-')
plt.xlabel('K')
plt.ylabel('SSE')
plt.title('Elbow Method using SSE')
plt.show()

from sklearn.metrics import silhouette_score
silhouette_scores = [ silhouette_score(X, model.labels_) for model in kmeans_per_k]
# Rysujemy wykres k vs wynik i wybieramy największą wartość:
from matplotlib import pyplot as plt
plt.figure(figsize=(8, 3))
plt.plot(range(2, 10), silhouette_scores, "bo-")
plt.ylabel("Silhouette score", fontsize=14)
plt.grid()
plt.show()