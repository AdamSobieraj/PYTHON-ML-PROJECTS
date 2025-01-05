from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier # drzewo decyzyjne -> tree
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

x, y = load_simple_classifier_dataset()

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

clf = DecisionTreeClassifier()
clf_2 = DecisionTreeClassifier()

print("fitting - training...")
clf.fit(X_train, y_train)

print("training on whole dataset...")
clf_2.fit(x, y)

print("predicting...")
y_pred = clf.predict(X_test)

# wpisujemy wartości dla pierwszych 10 predykcji

print("true values ", y[:10]) # -> y_true[:10]
print("predicted   ", y_pred[:10])

print("scoring...")

clf_score = clf.score(X_train, y_train)
print("Train score = ", clf_score)
clf_score = clf.score(X_test, y_test)
print("Test score = ", clf_score)

clf_score = clf_2.score(x, y)
print("whole set score = ", clf_score)