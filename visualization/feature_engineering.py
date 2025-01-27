# manipulacja danymi

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# wizualizacja

# Raport,do tworzenia podstawowego EDA

# data
titanic_train = pd.read_csv('../dataset/stat/titanic.csv')
print(titanic_train)

# notatnik
# print("---------------------EDA (Exploratory Data Analysis)------------------------")
# profile = ProfileReport(titanic_train, title="Titanic -  Report")
# print(profile)


print("---------------------1 missing data check------------------------")
print(titanic_train.isnull().mean())

print("---------------------2 data describe------------------------")
print(titanic_train.describe())

print("---------------------3 data coppy------------------------")
titanic_train_prepared = titanic_train.copy()
print(titanic_train_prepared)

print("---------------------4 remove unneded data------------------------")
titanic_train_prepared.drop(['PassengerId'], axis=1, inplace=True)
print(titanic_train_prepared)

print("---------------------5 zmienna objaśniana procent count survive------------------------")
print(titanic_train_prepared['Survived'].value_counts(normalize=True))

print("---------------------6 zmienna objaśniająca------------------------")
print(titanic_train_prepared['Pclass'].value_counts(normalize=True))
print(titanic_train_prepared)

print("---------------------7 plot the class------------------------")
sns.barplot(x='Pclass', y='Survived', data=titanic_train_prepared)
plt.show()

print("---------------------8  OHE (One Hot Encoder)-----------------------")
titanic_train_prepared = pd.concat([titanic_train_prepared, pd.get_dummies(titanic_train_prepared['Pclass'], drop_first=True)],  axis=1)
print(titanic_train_prepared)

print("---------------------9 convert name to state sex------------------------")
titanic_train_prepared['Title'] = titanic_train_prepared['Name'].str.split(', ', expand=True)[1].str.split('.',  expand=True)[0]
titanic_train_prepared.drop(['Name'], axis=1, inplace=True)
print(titanic_train_prepared)

plt.figure(figsize=(20, 9))
sns.barplot(x='Title', y='Survived', data=titanic_train_prepared)
plt.show()

print("---------------------10 check title occurnence------------------------")
print(titanic_train_prepared['Title'].value_counts(normalize=True))

print("---------------------11 reduce------------------------")
titanic_train_prepared.loc[~titanic_train_prepared['Title'].isin(['Mr', 'Miss', 'Mrs']), 'Title'] = 'Other'
print(titanic_train_prepared)

print("---------------------12 Zmienna Title to również zmienna kategoryczna------------------------")
titanic_train_prepared = pd.concat([titanic_train_prepared, pd.get_dummies(titanic_train_prepared['Title'], drop_first=True)], axis=1)
titanic_train_prepared.drop(['Title'], axis=1, inplace=True)
print(titanic_train_prepared)

print("---------------------13 Płeć. Również zmienna kategoryczna, jednak binarna ------------------------")
titanic_train_prepared = pd.concat([titanic_train_prepared, pd.get_dummies(titanic_train_prepared['Sex'], drop_first=True)], axis=1)
titanic_train_prepared.drop(['Sex'], axis=1, inplace=True)
print(titanic_train_prepared)

print("---------------------14 Wiek. Jest to zmienna numeryczna------------------------")
sns.boxplot(y='Age', x='Survived', data=titanic_train_prepared)
plt.show()

titanic_train_prepared['Age'].hist()

print("---------------------15 verify if child------------------------")
# jeśli wiek niższy niż 18 lat to jest to dziecko
titanic_train_prepared.loc[titanic_train_prepared['Age']<18, 'Child'] = 1

# osoba która nie jest dzieckiem otrzymała wartość 0
titanic_train_prepared.loc[titanic_train_prepared['Child']!=1, 'Child'] = 0
sns.barplot(x='Child', y='Survived', data=titanic_train_prepared)
plt.show()

age_median = titanic_train_prepared['Age'].median()
titanic_train_prepared['Age'] = titanic_train_prepared['Age'].fillna(age_median)
print(titanic_train_prepared)

print("---------------------16 remove unnecessary data------------------------")
