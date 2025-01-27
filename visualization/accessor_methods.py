import math
import pandas as pd
import numpy as np


print("-----------------------data----------------------")
df = pd.read_excel('../dataset/pivot/Pivot.xlsx')
print(df.head())

df['Data'] = pd.to_datetime(df['Data'])
print(df['Data'].dt.day_name().head())
print(df['Data'].dt.month_name().head())
print(df['Data'].dt.is_month_start.head())

print("-----------------------data filter----------------")
print(df[df['Data'].dt.day_name()=='Thursday'].head())

print("-----------------------string----------------------")
print(df['Produkt'].str.upper().head())
print(df[df['Region'].str.contains('Zachód')].sample(5))