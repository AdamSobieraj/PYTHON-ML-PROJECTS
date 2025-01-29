import numpy_example as np
import pandas as pd
import missingno as msno

df_with_nulls = pd.DataFrame({'A':[1,100,np.nan,1000,10000],
                             'B':[2,4,2,4,np.nan],
                             'C':[40,np.nan,20,np.nan,np.nan]})
print(df_with_nulls)

print("-------------- check missing data---------------------")
print(df_with_nulls.isnull().mean())
print()
print(df_with_nulls.isnull().sum())

print("-----------------check null for C---------------------")
print(df_with_nulls[df_with_nulls['C'].isnull()])

print("--------------graph with missing data-----------------")
msno.matrix(df_with_nulls)

print("-----------remove if two in row blank-----------------")
print(df_with_nulls.dropna(thresh=2))

print("----------remove columns with blank------------------")
print(df_with_nulls.dropna(thresh=3,axis=1))

print("----------fill nan with defined value----------------")
print(df_with_nulls.fillna('NOWA WARTOŚĆ'))

print("----------------with method fill---------------------")
print(df_with_nulls['B'].fillna(df_with_nulls['B'].mean()))


