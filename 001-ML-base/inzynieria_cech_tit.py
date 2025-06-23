# manipulacja danymi
import numpy as np
# import ydata as pd
import pandas as pd
# wizualizacja
import matplotlib.pyplot as plt
import seaborn as sns
# Raport,do tworzenia podstawowego EDA
# from ydata_profiling.profile_report import ProfileReport

# Wczytanie danych
titanic_train = pd.read_csv('../dataset/titanic/Titanic_train.csv')
print("------------------Raw data------------------")
print(titanic_train)
print("------------------info------------------")
print(titanic_train.info())

# # Explorator Data Analysys
# profile = ProfileReport(titanic_train, title="Titanic - Report")
# profile

# percent null
print(titanic_train.isnull().mean())

# Data coppy
titanic_train_prepared = titanic_train.copy()

# Every variable analyzys

## passanger id is not giving any information (remove)
titanic_train_prepared.drop(['PassengerId'], axis=1, inplace=True)

## count surviving rate (in percent)
print(titanic_train_prepared['Survived'].value_counts(normalize=True))

## Check class
print(titanic_train_prepared['Pclass'].value_counts(normalize=True))

## Plot class per surviwers
sns.barplot(x='Pclass', y='Survived', data=titanic_train_prepared)
plt.show()

## OHE (One Hot Encoder)
titanic_train_prepared = pd.concat([titanic_train_prepared,
pd.get_dummies(titanic_train_prepared['Pclass'],
drop_first=True)], axis=1)
print(titanic_train_prepared)\

## From name extract prefix, gives info women or man
titanic_train_prepared['Title'] = (
    titanic_train_prepared['Name'].str.split(', ',expand=True)[1].str.split('.', expand=True))[0]
titanic_train_prepared.drop(['Name'], axis=1, inplace=True)
print(titanic_train_prepared)

## Title vs survive
plt.figure(figsize=(20, 9))
sns.barplot(x='Title', y='Survived', data=titanic_train_prepared)
plt.show()

## Count titles
titanic_train_prepared['Title'].value_counts(normalize=True)

## Title shorten
titanic_train_prepared.loc[~titanic_train_prepared['Title'].isin(['Mr',
'Miss', 'Mrs']), 'Title'] = 'Other'
print(titanic_train_prepared)

titanic_train_prepared = pd.concat([titanic_train_prepared,
pd.get_dummies(titanic_train_prepared['Title'], drop_first=True)],
axis=1)
titanic_train_prepared.drop(['Title'], axis=1, inplace=True)
print(titanic_train_prepared)

##Sex
titanic_train_prepared = pd.concat([titanic_train_prepared,
pd.get_dummies(titanic_train_prepared['Sex'], drop_first=True)],
axis=1)
titanic_train_prepared.drop(['Sex'], axis=1, inplace=True)
print(titanic_train_prepared)

## Display survive per age
sns.boxplot(y='Age', x='Survived', data=titanic_train_prepared)
plt.show()

## Age distribution
titanic_train_prepared['Age'].hist()

# je?li wiek ni?szy ni? 18 lat to jest to dziecko
titanic_train_prepared.loc[titanic_train_prepared['Age']<18,'Child'] = 1

# osoba która nie jest dzieckiem otrzyma?a warto?? 0
titanic_train_prepared.loc[titanic_train_prepared['Child']!=1,'Child'] = 0
sns.barplot(x='Child', y='Survived', data=titanic_train_prepared)
plt.show()

age_median = titanic_train_prepared['Age'].median()
titanic_train_prepared['Age'] = titanic_train_prepared['Age'].fillna(age_median)
print(titanic_train_prepared)

