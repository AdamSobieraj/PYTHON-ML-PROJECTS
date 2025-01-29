import numpy_example as np
import pandas as pd

exam1 = [89, 85, 93, 83]
labels = ['Student A', 'Student B', 'Student C', 'Student D']

print(pd.Series(exam1, labels))

print(pd.Series(exam1, labels)['Student D'])

data = {s: p for s, p in zip(labels, exam1)}

print(data)

print(pd.Series(data))

exam2 = [74, 56, 44, 92]

e1 = pd.Series(exam1, labels)
e2 = pd.Series(exam2, labels)

# zsumować

print(e1 + e2)
print(e1 * e2)
print(e1 / e2)

df = pd.DataFrame({'e1': exam1, 'e2': exam2}, index=labels)
print(df)
print(df['e1'])
print(type(df['e1']))

data = np.array([exam1, exam2])
data.transpose()
print(data)
df = pd.DataFrame(data.transpose(), index=labels, columns=['e1', 'e2'])
print(df)

# zamienić DataFrame na ndarray.

df.to_numpy()
print(df.to_numpy())

# shape
print(df.shape)

# Dodanie kolumny z wartościami ,Należy pamiętać, że nowy wektor powinien mieć tyle samo elementów co pozostałe.

df['e3'] = [67, 59, 79, 84]
print(df)

df['semester1'] = df['e1'] + df['e2'] + df['e3']
print(df)

# Jeśli chcemy wybrać więcej niż jedną kolumnę – wystarczy, że w nawiasie kwadratowym podamy listę interesujących nas kolumn.

print(df[['e1', 'e2']])

# Spróbujmy wyciągnąć wyłącznie informacje dotyczące Studenta C. W tym celu wykorzystamy metodę loc.

print(df.loc['Student C'])
print(df.loc['Student C', 'e2'])
print(df.loc[['Student C', 'Student D'], ['e2']])
print(df.iloc[1])

# wyrażenia logiczne
print(df['e2'] > 70)
print(df[df['e2'] > 70])
print(df[(df['e2'] < 50) | (df['e2'] > 90)])

# usówanie kolumny
print("----------------------------------------")
df['semester1'] = df['e1'] + df['e2'] + df['e3']
print(df)
df2 = df.drop('semester1', axis=1)
print("DF2")
print(df2)
print("DF")
print(df)
print("----------------------------------------")
print("-------------permanent del--------------")
# usówanie permanentne
df.drop(['e3', 'semester1'], axis=1, inplace=True)
print(df)
print("---------row permanent del--------------")
df.drop('Student B', inplace=True)
print(df)
print("---------index reset not permanent------")
print(df.reset_index())
print("------Sposób 1 – funkcja set_index------")
df_new_index = df.reset_index()
print(df_new_index)
df_new_index['student_name'] = ['Adrian', 'Bartłomiej', 'Celina']
df_new_index.set_index('student_name', inplace=True)
print(df_new_index)
print("------Sposób 2 - zmiany bezpośrednio na atrybucie index------")
df_new_index2 = df.reset_index()
print(df_new_index2)
df_new_index2.index = ['Adrian', 'Bartłomiej', 'Celina']
print(df_new_index)
print("------column rename------")
df.rename(columns={'e1': 'exam1', 'e2': 'exam2', 'e3': 'exam3'}, inplace=True)
print(df)
print("------column rename by index------")
df.rename(index={'Student C': 'Student CC'}, inplace=True)
print(df)
print("------column rename to capital------")
df.rename(str.upper, axis='columns', inplace=True)
print(df)

print("------dataframe value reset------")
df = pd.DataFrame({'A': [100, 44, 56, 99, 85, 100],
                   'B': ['Panda', 'Snake', 'Snake', 'Rat', 'Dog', 'Panda']})

print(df)

print("------Unique------")
print(df['B'].unique())
print("------nunique------")
print(df['B'].nunique())
print("------count occurnence------")
print(df['B'].value_counts())
print("------count occurnence with procent count------")
print(df['B'].value_counts(normalize=True))
print("------sort------")
print(df.sort_values(by='A'))
print("------sort with order dir------")
print(df.sort_values(by='A', ascending=False))
print("------drop_duplicates------")
print(df.drop_duplicates())
print(df.drop_duplicates(subset=['B']))

print("------Indexing------")
exam1 = [89, 85, 93, 83]
exam2 = [74, 56, 44, 92]
exam3 = [67, 59, 79, 84]
df = pd.DataFrame({'e1': exam1, 'e2': exam2, 'e3': exam3}, index=labels)
df['semester1'] = df['e1'] + df['e2'] + df['e3']

print(df)

print("------Sposób nr 1 – MultiIndex.from_tuples------")
schools = ['High School X', 'High School X', 'High School Y', 'High School Y']
multi_index_list = [(school, student) for school, student in zip(schools, df.index)]
print(multi_index_list)
df.index = pd.MultiIndex.from_tuples(multi_index_list, names=['School', 'Student'])
print(df)
print("------Sposób nr 2 - funkcja set_index------")
df.set_index([pd.Index(['High School X', 'High School X', 'High School Y', 'High School Y']), df.index], inplace=True)
print(df)
df.index.names = ['School', 'School', 'Student']
print(df)
print("------locate------")
print(df.loc['High School X'])
print(df.loc['High School X'].iloc[1])
print("------drop_duplicates------")
print(df.xs('High School Y'))
# print(df.xs(('High School Y','Student D')))
# print(df.xs('Student D',level='Student'))

print("------new data for group by------")
df = pd.DataFrame({'Category': ['Games', 'Games', 'Games','Film&Video', 'Film&Video', 'Film&Video'],
                   'Project_Title': ['The Last Faith', 'Magic Puzzles', 'Dinosaur Fossil Hunter',
                                     'Beyond Your Eyes', '5150', '8-Bit Wars'],
                   'Pledged': [92774, 2873519, 7962, 276, 23963, 6950],
                   'Country': ['UK', 'USA', 'Poland','Bulgaria', 'USA', 'UK'],
                   'Date_Start': ['2020-03-21', '2020-03-11', '2020-04-16',
                                  '2020-02-09', '2020-04-10', '2020-03-19']})
print(df)
print("------grup by category------")
print(df.groupby('Category').sum())
# print("------mean------")
# print(df.groupby('Category').mean())
print("------count------")
print(df.groupby('Category').count())

print("------data time from strig to time format------")
df['Date_Start'] = pd.to_datetime(df['Date_Start'])

print(df.groupby(pd.Grouper(key='Date_Start',freq='ME')).sum())
test = df.groupby(pd.Grouper(key='Date_Start',freq='ME')).agg({'Pledged':'sum','Project_Title':'count'})
print(test)

print("------drop_duplicates------")