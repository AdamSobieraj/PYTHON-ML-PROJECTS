# Importowanie niezbędnych bibliotek
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Generowanie przykładowych danych
# Przygotowanie danych:
# Generujemy 100 punktów danych
# X to zmienna niezależna (wartości od 0 do 10)
# y to zmienna zależna (2X + 1 + szum losowy)
# Szum losowy symuluje rzeczywiste odchylenia
np.random.seed(42)  # Ustawienie ziarna losowego dla powtarzalności
X = np.linspace(0, 10, 100).reshape(-1, 1)  # Zmienna niezależna (X)
y = 2 * X + 1 + np.random.normal(0, 1, (100, 1))  # Zmienna zależna (y)

# Podział danych na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Utworzenie i trenowanie modelu
model = LinearRegression()
model.fit(X_train, y_train)

# Pobranie parametrów modelu
wspolczynnik = model.coef_[0][0]  # Współczynnik kierunkowy (a)
wyraz_wolny = model.intercept_[0]  # Wyraz wolny (b)

# Obliczenie predykcji
y_pred = model.predict(X_test)

# Obliczenie metryk oceny modelu
R2 = model.score(X_test, y_test)  # Współczynnik determinacji
bład_sredni = np.mean((y_test - y_pred) ** 2)  # Średni błąd kwadratowy

# Wyświetlenie wyników
print(f"Równanie regresji: y = {wspolczynnik:.2f}x + {wyraz_wolny:.2f}")
print(f"Współczynnik determinacji (R²): {R2:.3f}")
print(f"Średni błąd kwadratowy: {bład_sredni:.3f}")

# Wizualizacja
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Dane testowe')
plt.plot(X_test, y_pred, color='red', label='Linia regresji')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Regresja liniowa')
plt.legend()
plt.grid(True)
plt.show()