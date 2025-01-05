from sklearn.tree import DecisionTreeClassifier # drzewo decyzyjne -> tree
from sklearn.svm import SVC # typ SVM, czyli po kropce jest svm
from sklearn.neighbors import KNeighborsClassifier # model k najbliższych sąsiadów
from sklearn.datasets import make_classification

# Prosty zbiór danych dostarczający losowe dane obiektów dwóch klas,
# Aby przerobić na obiekty 3 klas, należy dodać kolejny element listy
# weights, odpowiednio dopasować wagi, tak aby suma wynosiła 1.

"""
    Przykład tworzenia prostego zbioru danych
"""
def load_simple_classifier_dataset(weights=[0.5, 0.5]):
    """
        Metoda generująca prosty zbiór danych

        Argumenty:
            weights - lista z udziałami obiektów każdej klasy w próbce,
                      ich suma musi wynosić 1

        Zwraca:
            X - dane wejściowe dla modelu
            y - true labels dla tych danych wejściowych
    """

    X, y = make_classification(
        n_samples=1000,
        n_classes=len(weights),
        n_informative=len(weights),
        weights=weights,
        flip_y=0,
        random_state=1
    )

    return X, y

# stworzenie klasyfikatorów
dt_clf = DecisionTreeClassifier()
svc_clf = SVC()
knn_clf = KNeighborsClassifier()

# stworzenie pełnego pipeline'u ML
x, y = load_simple_classifier_dataset()

# wrzucamy wszystkie klasyfikatory do jednej listy
klasyfikatory = [dt_clf, svc_clf, knn_clf]

for clf in klasyfikatory:
    print("--------------")
    print("fitting - training...")
    clf.fit(x, y)

    print("predicting...")
    y_pred = clf.predict(x)

    # wpisujemy wartości dla pierwszych 10 predykcji

    print("true values ", y[:10])
    print("predicted   ", y_pred[:10])

    print("scoring...")

    clf_score = clf.score(x, y)
    print("score = ", clf_score)

# fit(x, y) – metoda służąca do wyszkolenia modelu.
# Niczego nie zwraca. Wywołuje się ją tak samo, jak każdą metodę klasy w Pythonie.
# Przyjmuje dwa argumenty:
#
# x – dane wejściowe
# y – dane wyjściowe, które chcemy osiągnąć (true labels)
#
# predict(x) – metoda służąca do predykcji wyjścia modelu, bazując
# na dostarczonym wejściu. Metoda ta zwraca tablicę z przewidzianymi
# wyjściami modelu. Przyjmuje jeden argument:
#
# x – dane wejściowe, dla których chcemy przewidzieć wyjście
# score(x, y) – metoda zwracająca metrykę, bazując na dostarczonym wejściu.
# Metoda ta zwraca wynik w postaci liczby zmiennoprzecinkowej. Przyjmuje dwa argumenty:
#
# x — dane wejściowe
# y — dane wyjściowe, które chcemy osiągnąć (true labels)