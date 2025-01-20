import numpy as np

from statisticFunction import preform_stat

# Generowanie 100 elementów
data_100 = np.random.normal(loc=3, scale=1, size=100)

# Generowanie 10 000 elementów
data_10000 = np.random.normal(loc=3, scale=1, size=10000)

print(f"Średnia dla 100 elementów: {np.mean(data_100)}")
print(f"Odchylka standardowa dla 100 elementów: {np.std(data_100)}")

print(f"\nŚrednia dla 10 000 elementów: {np.mean(data_10000)}")
print(f"Odchylka standardowa dla 10 000 elementów: {np.std(data_10000)}")

preform_stat(data_100)
preform_stat(data_10000)

print("Podsumowanie")
print("Analiza statystyk opisowych dla obu zestawów danych pokazuje, "
      "że mimo różnic w liczbie elementów, statystyki są bardzo podobne. "
      "To spowodowane jest tym, że oba zestawy mają te same parametry "
      "rozkładu normalnego (średnia 3, odchylenie standardowe 1).")