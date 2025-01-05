import numpy as np
from sklearn.datasets import load_digits, load_wine, load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

# Wybieramy generator danych
datasets = {
    "digits": load_digits(),
    "wine": load_wine(),
    "iris": load_iris()
}

# Przygotowanie i podział zbiorów danych
for dataset_name, dataset in datasets.items():
    X = dataset.data
    y = dataset.target

    # Standardizacja danych
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Podział na zbiory treningowe i testowe
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    print(f"\nAnaliza dla {dataset_name}:")

    # Wybór klasyfikatorów
    classifiers = {
        "SVC": SVC(kernel='rbf', C=1),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "KNN": KNeighborsClassifier(n_neighbors=5)
    }

    # Trening modeli i obliczenie metryk
    for name, clf in classifiers.items():
        clf.fit(X_train, y_train)

        y_pred_train = clf.predict(X_train)
        y_pred_test = clf.predict(X_test)

        accuracy_train = accuracy_score(y_train, y_pred_train)
        accuracy_test = accuracy_score(y_test, y_pred_test)

        print(f"\n{name}:\n"
              f"Treningowa dokładność: {accuracy_train:.4f}\n"
              f"Dokładność testowa: {accuracy_test:.4f}")

        print(classification_report(y_test, y_pred_test))

        # Analiza nadmiernego dopasowania
        if accuracy_train > accuracy_test * 1.05:
            print("Model wykazuje znak nadmiernego dopasowania!")
        elif accuracy_train < accuracy_test * 0.95:
            print("Model może być zbyt ogólny.")
        else:
            print("Model wydaje się równomiernie dobrze dopasowany.")

print("\nZakończenie analizy.")


# Analiza dla zestawu danych "digits"
# SVC (Support Vector Classifier):
# Model nie wykazuje znaków nadmiennego dopasowania
# Decision Tree:
# Model wykazuje znak nadmiennego dopasowania
# Random Forest:
# Model nie wykazuje znaków nadmiennego dopasowania
# Logistic Regression:
# Model nie wykazuje znaków nadmiennego dopasowania
# KNN (K-Nearest Neighbors):
# Model nie wykazuje znaków nadmiennego dopasowania
# Analiza dla zestawu danych "wine"
# SVC:
# Model nie wykazuje znaków nadmiennego dopasowania
# Decision Tree:
# Model wykazuje znak nadmiennego dopasowania
# Random Forest:
# Model nie wykazuje znaków nadmiennego dopasowania
# Logistic Regression:
# Model nie wykazuje znaków nadmiennego dopasowania
# KNN:
# Model nie wykazuje znaków nadmiennego dopasowania
# Analiza dla zestawu danych "iris"
# SVC:
# Model nie wykazuje znaków nadmiennego dopasowania
# Decision Tree:
# Model nie wykazuje znaków nadmiennego dopasowania
# Random Forest:
# Model nie wykazuje znaków nadmiennego dopasowania
# Logistic Regression:
# Model nie wykazuje znaków nadmiennego dopasowania
# KNN:
# Model nie wykazuje znaków nadmiennego dopasowania

# Podsumowanie: Wszystkie modele pokazują bardzo dobre wyniki dla wszystkich trzech zestawów danych.
