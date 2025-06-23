from sklearn.datasets import load_iris
from sklearn.model_selection import KFold


iris = load_iris()
X, y, iris_classes = iris.data, iris.target, iris.target_names

kf = KFold(n_splits=5, shuffle=True, random_state=10)

for fold_nr, (train_idx, test_idx) in enumerate(kf.split(X)):
    X_train = X[train_idx]
    X_test = X[test_idx]
    y_train = y[train_idx]
    y_test = y[test_idx]

# Użycie enumerate pozwala uzyskać numer aktualnego foldu.
# Ponieważ chcemy uzyskać niezależną ocenę naszego modelu dla każdego
# foldu, tworzymy osobny model i osobno go trenujemy i ewaluujemy.
# Wytrenowane modele możemy zapisać do tablicy czy słownika, aby mieć do
# nich dostęp w przyszłości.


# Teraz wewnątrz foldu wytrenuj model na danych treningowych, określ jego
# wynik na danych testowych, zapisz wynik i model w odpowiednich tablicach.

import numpy as np
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier

scaler = StandardScaler()
kf = KFold(n_splits=5, shuffle=True, random_state=1)

models = []
scores = []

for fold_nr, (train_idx, test_idx) in enumerate(kf.split(X)):
    X_train = X[train_idx]
    X_test =X[test_idx]
    y_train = y[train_idx]
    y_test = y[test_idx]

# skalowanie danych wejściowych, aby model lepiej dzia?a?
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

clf = SGDClassifier(random_state=1).fit(X_train, y_train)
models.append(clf)
scores.append(clf.score(X_test, y_test))
print("wyniki poszczególnych foldów: ", scores)
print("Średni wynik wszystkich foldów: ", np.array(scores).mean())

# Z wrapperem

from sklearn.model_selection import cross_val_score

# stworzenie klasyfikatora
clf = SGDClassifier(random_state=1)
# użycie metody cross_val_score do sprawdzenia
# działania naszego modelu na różnych podziałach
cv_score = cross_val_score(clf, X, y, cv=5)
print("wynik kroswalidacji: ", cv_score)
print("?redni wynik wszystkich foldów: ", cv_score.mean())

# podziałem za pomocą train_test_split bez użycia stratyfikacji:
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

X, y = make_classification(
                            n_samples=1000,
                            n_classes=2,
                            weights=[0.99, 0.01],
                            flip_y=0,
                            random_state=1
                            )

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=3)
train_0, train_1 = len(y_train[y_train==0]), len(y_train[y_train==1])
test_0, test_1 = len(y_test[y_test==0]), len(y_test[y_test==1])
print('>Train: 0=%d, 1=%d, Test: 0=%d, 1=%d' % (train_0, train_1,
test_0, test_1))

# z strtify
# Przepisanie powyższego przykładu, aby dane były rozłożone równomiernie w
# zbiorze treningowych i testowym:

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=3,stratify=y)
train_0, train_1 = len(y_train[y_train==0]), len(y_train[y_train==1])
test_0, test_1 = len(y_test[y_test==0]), len(y_test[y_test==1])
print('>Train: 0=%d, 1=%d, Test: 0=%d, 1=%d' % (train_0, train_1,
test_0, test_1))