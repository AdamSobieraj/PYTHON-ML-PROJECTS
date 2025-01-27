import math
import pandas as pd
import numpy as np


print("-----------------------data----------------------")
df = pd.read_excel('../dataset/pivot/Pivot.xlsx')
print(df.head())

def commission_fee(x):
    if x <= 300:
        return 0
    elif x <= 900:
        return x * 0.03
    else:
        return x * 0.06

print("------------------data operation and save to column------------")
df['commission_fee'] = df['Sprzedaż'].apply(lambda x: commission_fee(x))
print(df)

print("------------------data operation and save to column------------")
df['Produkt_len'] = df['Produkt'].apply(len)
print(df)

print("------------------data operation and save to column------------")
df['#_opakowań'] = df['Sztuki'].apply(lambda x: math.ceil(x/5))


print("------------------data operation and save to multiple column------------")
def bonus(row):

    margin = (row['Sprzedaż'] - row['Koszty'])/row['Sprzedaż']

    if margin > 0.55:
        return 200
    else:
        return 0

df['Bonus'] = df.apply(lambda row: bonus(row),axis=1)
df.sample(10)
print(df)

print("-----------------------data map----------------------")
car_dict = dict(zip(df['Przedstawiciel'].unique(),['Mazda','Toyota','BMW','Audi','Fiat','Seat']))
print(car_dict)

df['Marka_samochodu'] = df['Przedstawiciel'].map(car_dict)
print(df)

# print("-----------------------data applymap----------------------")
# df.applymap(lambda x: x.upper() if isinstance(x,str) else x)
# print(df)
# df.map(lambda x: x.upper() if isinstance(x,str) else x)
# print(df)