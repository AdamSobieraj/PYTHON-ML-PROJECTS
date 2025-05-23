# manipulacja danymi
import numpy as np
import pandas as pd

# wizualizacja danych
import matplotlib.pyplot as plt
import seaborn as sns

# statystyczna analiza danych
from scipy import stats

# przygotowanie danych
from sklearn.preprocessing import StandardScaler, MinMaxScaler

dataset = pd.read_csv('../dataset/stat/titanic.csv')
print(dataset)

fare_values = dataset.loc[dataset['Fare'].notnull(), 'Fare'].values
print(fare_values.shape)

plt.hist(fare_values, bins=20)
plt.show()

#Średnia
mean_fare = np.round(np.mean(fare_values))
print(mean_fare)
plt.hist(fare_values, bins=20)
plt.axvline(x = mean_fare, color='red', label ='Średnia')
plt.legend(loc='upper right')
plt.show()

#Mediana
median_fare = np.median(fare_values)
print(median_fare)
plt.hist(fare_values, bins=20)
plt.axvline(x = mean_fare, color='red', label ='Średnia')
plt.axvline(x = median_fare, color='green', label ='Mediana')
plt.legend(loc='upper right')
plt.show()

#Moda
mode_fare = stats.mode(fare_values)
print(mode_fare)
plt.hist(fare_values, bins=20)
plt.axvline(x = mean_fare, color='red', label ='Średnia')
plt.axvline(x = median_fare, color='green', label ='Mediana')
plt.axvline(x = mode_fare[0], color='orange', label ='Moda')
plt.legend(loc='upper right')
plt.show()

#Kwartyle
q0 = np.quantile(fare_values, 0.0)
q1 = np.round(np.quantile(fare_values, 0.25))
q3 = np.round(np.quantile(fare_values, 0.75))
q4 = np.round(np.quantile(fare_values, 1.0))
print(f'Q0: {q0}')
print(f'Q1: {q1}')
print(f'Q2: {median_fare}')
print(f'Q3: {q3}')
print(f'Q4: {q4}')
plt.hist(fare_values, bins=20)
plt.axvline(x = mean_fare, color='red', label ='Średnia')
plt.axvline(x = median_fare, color='green', label ='Mediana')
plt.axvline(x = mode_fare[0], color='orange', label ='Moda')
plt.axvline(x = q0, color='black', label = 'Min')
plt.axvline(x = q1, color='black', label = 'Q1')
plt.axvline(x = q3, color='black', label = 'Q3')
plt.axvline(x = q4, color='black', label = 'Max')
plt.legend(loc='upper right')
plt.show()

#Zakres
range_fare = max(fare_values) - min(fare_values)
print(range_fare)

#Rozstęp międzykwartylowy - IQR
iqr = q3 - q1
print(iqr)
plt.boxplot(fare_values)
plt.show()

#Wariancja
variance_fare = np.var(fare_values, ddof=1)
print(variance_fare)

#Odchylenie standardowe
print(variance_fare ** (1 / 2))
standard_deviation_fare = np.std(fare_values, ddof=1)
print(standard_deviation_fare)

#Asymetria rozkładu
scaler_standardized = StandardScaler()
standardized_fare_values = scaler_standardized.fit_transform(fare_values.reshape(-1, 1))
plt.hist(standardized_fare_values, bins=20)
plt.axvline(x = standardized_fare_values.mean(), color='red', label = 'Średnia')
plt.show()
print(f'Średnia: {standardized_fare_values.mean()}')
print(f'Odchylenie standardowe: {np.std(standardized_fare_values, ddof=1)}')

scaler_MinMax = MinMaxScaler()
normalized_fare_values = scaler_MinMax.fit_transform(fare_values.reshape(-1, 1))
plt.hist(normalized_fare_values, bins=20)
plt.axvline(x = normalized_fare_values.mean(), color='red', label = 'Średnia')
plt.show()
print(f'Średnia: {normalized_fare_values.mean()}')
print(f'Odchylenie standardowe: {np.std(normalized_fare_values, ddof=1)}')

#Korelacja
sibsb_values = dataset.loc[dataset['Fare'].notnull(), 'SibSp'].values
plt.scatter(x=fare_values, y=sibsb_values, alpha=0.5)
plt.xlabel('fare')
plt.ylabel('SibSp')
plt.show()
stats.pearsonr(fare_values, sibsb_values)