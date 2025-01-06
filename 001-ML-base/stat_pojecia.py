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

# data
dataset = pd.read_csv('../dataset/stat/titanic.csv')
print(dataset)

# age wartości bez null
age_values = dataset.loc[dataset['Age'].notnull(), 'Age'].values
print('Values nonnull count')
print(age_values.shape)

# przedstawienie na histogramie
plt.hist(age_values, bins=20)
plt.show()

# Policzmy średnią dla naszego zbioru, którą następnie zaokrąglimy:
mean_age = np.round(np.mean(age_values))
print(mean_age)
#Nanieśmy tę wartość na histogram
plt.hist(age_values, bins=20)
plt.axvline(x = mean_age, color='red', label = 'Średnia')
plt.legend(loc='upper right')
plt.show()

#Policzmy teraz medianę wieku
median_age = np.median(age_values)
print(median_age)
#Nanieśmy tę wartość na histogram
plt.hist(age_values, bins=20)
plt.axvline(x = mean_age, color='red', label = 'Średnia')
plt.axvline(x = median_age, color='green', label = 'Mediana')
plt.legend(loc='upper right')
plt.show()

# Moda
mode_age = stats.mode(age_values)
print(mode_age)
#Nanieśmy tę wartość na histogram
plt.hist(age_values, bins=20)
plt.axvline(x = mean_age, color='red', label = 'Średnia')
plt.axvline(x = median_age, color='green', label = 'Mediana')
plt.axvline(x = mode_age[0], color='orange', label = 'Moda')
plt.legend(loc='upper right')
plt.show()

# kwartyle dla zmiennej wiek
q0 = np.quantile(age_values, 0.0)
q1 = np.round(np.quantile(age_values, 0.25))
q3 = np.round(np.quantile(age_values, 0.75))
q4 = np.round(np.quantile(age_values, 1.0))
print(f'Q0: {q0}')
print(f'Q1: {q1}')
print(f'Q2: {median_age}')
print(f'Q3: {q3}')
print(f'Q4: {q4}')
#Nanieśmy tę wartość na histogram
plt.hist(age_values, bins=20)
plt.axvline(x = mean_age, color='red', label = 'Średnia')
plt.axvline(x = median_age, color='green', label = 'Mediana')
plt.axvline(x = mode_age[0], color='orange', label = 'Moda')
plt.axvline(x = q0, color='black', label = 'Min')
plt.axvline(x = q1, color='black', label = 'Q1')
plt.axvline(x = q3, color='black', label = 'Q3')
plt.axvline(x = q4, color='black', label = 'Max')
plt.legend(loc='upper right')
plt.show()

# Zakres
range_age = max(age_values) - min(age_values)
print(range_age)

# Rozstęp międzykwartylowy - IQR
iqr = q3 - q1
print(iqr)
# boxplot
plt.boxplot(age_values)
plt.show()

# wariancja
variance_age = np.var(age_values, ddof=1)
print(variance_age)

# Odchylenie standardowe
print(variance_age**(1/2))
# lub
standard_deviation_age = np.std(age_values, ddof=1)
print(standard_deviation_age)

# Rozkład danych Standaryzacja
scaler_standardized = StandardScaler()
standardized_age_values = scaler_standardized.fit_transform(age_values.reshape(-1, 1))
plt.hist(standardized_age_values, bins=20)
plt.axvline(x = standardized_age_values.mean(), color='red', label = 'Średnia')
plt.show()
print(f'Średnia: {standardized_age_values.mean()}')
print(f'Odchylenie standardowe: {np.std(standardized_age_values, ddof=1)}')

# Min Max Scaler
scaler_MinMax = MinMaxScaler()
normalized_age_values = scaler_MinMax.fit_transform(age_values.reshape(-1, 1))
plt.hist(normalized_age_values, bins=20)
plt.axvline(x = normalized_age_values.mean(), color='red', label = 'Średnia')
plt.show()
print(f'Średnia: {normalized_age_values.mean()}')
print(f'Odchylenie standardowe: {np.std(normalized_age_values, ddof=1)}')

# Korelacja

# korekta danych
sibsb_values = dataset.loc[dataset['Age'].notnull(), 'SibSp'].values
plt.scatter(x=age_values, y=sibsb_values, alpha=0.5)
plt.xlabel('Age')
plt.ylabel('SibSp')
plt.show()

# korelację Pearsona.
print(stats.pearsonr(age_values, sibsb_values))
