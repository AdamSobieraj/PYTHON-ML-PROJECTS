import numpy as np
import matplotlib.pyplot as plt

# Generowanie przykładowych danych
np.random.seed(42)
X = np.linspace(0, 10, 100).reshape(-1, 1)
y = 2 * X + 1 + np.random.normal(0, 1, (100, 1))

# Podział danych na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = X[:80], X[80:], y[:80], y[80:]


# Obliczanie parametrów regresji liniowej
# regresja liniowa -> liniowa czyli jej wzór jest wzorem na linie y = ax + b
def oblicz_regresje(X, y):
    # Obliczanie średnich
    x_srednie = np.mean(X)
    y_srednie = np.mean(y)

    # Obliczanie współczynnika kierunkowego (a)
    mianownik = np.sum((X - x_srednie) ** 2)
    licznik = np.sum((X - x_srednie) * (y - y_srednie))
    a = licznik / mianownik

    # Obliczanie wyrazu wolnego (b)
    b = y_srednie - a * x_srednie

    return a, b


# Obliczanie parametrów dla zbioru treningowego
a, b = oblicz_regresje(X_train, y_train)

# Obliczanie predykcji dla zbioru testowego
y_pred = a * X_test + b

# Obliczanie metryk oceny modelu
R2 = 1 - np.sum((y_test - y_pred) ** 2) / np.sum((y_test - np.mean(y_test)) ** 2)
bład_sredni = np.mean((y_test - y_pred) ** 2)

# Wyświetlenie wyników
print(f"Równanie regresji: y = {a:.2f}x + {b:.2f}")
print(f"Współczynnik determinacji (R²): {R2:.3f}")
print(f"Średni błąd kwadratowy: {bład_sredni:.3f}")

# Wizualizacja
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Dane testowe')
plt.plot(X_test, y_pred, color='red', label='Linia regresji')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Regresja liniowa (implementacja własna)')
plt.legend()
plt.grid(True)
plt.show()
