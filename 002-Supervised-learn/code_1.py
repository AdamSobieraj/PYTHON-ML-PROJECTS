import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

bike_data_raw = pd.read_csv('../dataset/Supervised/daily-bike-share.csv')

print(bike_data_raw)

# legenda
#instant – unikalny indeks.
# dteday – data.
# season – pora roku (1:zima, 2:wiosna, 3:lato, 4:jesień).
# yr – rok (0 = 2011, 1 = 2012).
# mnth – miesiąc (1:styczeń ... 12:Grudzień).
# holiday – wartość binarna wskazująca, czy obserwacja została przeprowadzona w dzień świąteczny, czy nie.
# weekday – dzień tygodnia, w którym dokonano obserwacji (0:niedziela ... 6:sobota).
# workingday – wartość binarna wskazująca, czy dany dzień jest dniem roboczym (nie weekendem ani świętem), czy nie.
# weathersit – wartość kategoryczna, wskazująca sytuację pogodową (1:bezchmurnie, 2:mgła/chmury, 3:lekki deszcz/śnieg, 4:ciężki deszcz/ogień/śnieg/mgła).
# temp – temperatura w stopniach Celsjusza (znormalizowana).
# atemp – temperatura odczuwalna w stopniach Celsjusza (znormalizowana).
# hum – poziom wilgotności (znormalizowany).
# windspeed – prędkość wiatru (znormalizowana).
# rentals – liczba wypożyczonych rowerów.

# sprawdzenie typu zmiennych
print(bike_data_raw.info())

# korekta stringu daty w celu odczytania przez kod poprawnie
bike_data_raw['dteday'] = pd.to_datetime(bike_data_raw['dteday'])
# display(bike_data_raw) -> dla notatnika
print("check typu")
print(bike_data_raw.info())
print("Dane po zmiane")
print(bike_data_raw)

# rozkład dla zmiennej objaśnianej rentals, która jest historyczną liczbą wypożyczonych rowerów.
print(bike_data_raw['rentals'].describe())

#c wykres
plt.figure(figsize=(16, 7))
plt.plot(bike_data_raw['dteday'], bike_data_raw['rentals'], label='Liczba wypożyczeń')
plt.plot(bike_data_raw['dteday'], bike_data_raw['rentals'].rolling(30).mean(), linewidth=3.0, label='30 dniowa średnia krocząca')
plt.xlim([bike_data_raw['dteday'].min(), bike_data_raw['dteday'].max()])
plt.ylim([0, bike_data_raw['rentals'].max()*1.025])
plt.legend(loc='upper left')
plt.show()

# usówanie kolum
#instant – unikalny indeks wiersza, ta zmienna nie jest informatywna,
# dteday – data, informacje z tej cechy są już zawarte w innych cechach,
# yr – rok 2011 już nie wróci.

print('Przed usunięciem:')
# display(bike_data_raw)
print('Po usunięciu:')
bike_data = bike_data_raw.copy()
bike_data.drop(['instant', 'dteday', 'yr'], axis=1, inplace=True)
# display(bike_data)
print(bike_data)

# skategoryzowanie
numeric_features = ['temp', 'atemp', 'hum', 'windspeed']
categorical_features = ['season','mnth','holiday','weekday','workingday','weathersit']
target = 'rentals'

# czy wraz ze wzrostem jednej cechy jest również tendencja dla innej cechy?
for numeric_feature in numeric_features:
    fig = plt.figure(figsize=(5, 2))
    plt.scatter(bike_data[numeric_feature], bike_data[target], alpha=0.25)
    plt.xlabel(numeric_feature)
    plt.ylabel('Bike Rentals')
    plt.title(f'rentals vs {numeric_feature}')
    plt.show()

# pairplot
fig = sns.pairplot(bike_data[[target]+numeric_features], kind='scatter', plot_kws={'alpha': 0.25})
fig.fig.set_size_inches(11, 11) #ustawiamy rozmiar wykresu
plt.show()

# wyliczenie korelacji
plt.figure(figsize=(8, 8))
ax = sns.heatmap(bike_data[[target]+numeric_features].corr(),
                 xticklabels=bike_data[[target]+numeric_features].corr().columns,
                 yticklabels=bike_data[[target]+numeric_features].corr().columns,
                 cmap='RdYlGn',
                 center=0,
                 annot=True)

plt.title('Korelacja zmiennych numerycznych dla zbioru bike dataset', fontsize=12)
bottom, top = ax.get_ylim()
ax.set_ylim(bottom + 0.5, top - 0.5)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

# tu sie kończy Inżynieria cech
###################################
# korekta na temp i temp odczuwalną
# Stworzyliśmy nową zmienną difference_temp, możemy zatem usunąć temperaturę
# odczuwalną i policzyć korelację raz jeszcze, choć teraz jedynie pomiędzy naszą
# zmienną zależną, temperaturą i właśnie stworzoną nową zmienną.

bike_data['difference_temp'] = (bike_data['atemp'] - bike_data['temp'])/bike_data['temp']
bike_data.drop(['atemp'], axis=1, inplace=True)
numeric_features = ['temp', 'difference_temp', 'hum', 'windspeed']
bike_data[['rentals', 'temp', 'difference_temp']].corr()

print(bike_data)

for categoric_features in categorical_features:
    plt.figure(figsize=(16, 3))
    sns.violinplot(y=bike_data[target], x=bike_data[categoric_features], palette="Set2")
    plt.show()