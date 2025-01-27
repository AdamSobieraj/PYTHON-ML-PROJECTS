import pandas as pd
import numpy as np

print("-----------------------data----------------------")
df = pd.read_excel('../dataset/pivot/Pivot.xlsx')
print(df.head())

print("-----------------------data aggregation----------------")
test = df.pivot_table(values='Sprzedaż',index='Przedstawiciel',columns='Region',aggfunc="sum")
print(test)

print("---------data aggregation with nan fill----------------")
print(df.pivot_table(values='Sprzedaż',index='Przedstawiciel',columns='Region',aggfunc="sum").fillna(0).round(2))

print("---------data aggregation with nan filland multi index---------")
print(df.pivot_table(values='Sprzedaż',index=['Region','Przedstawiciel'],aggfunc="sum").round(2))

print("---------data aggregation with nan filland multi index---------")
print(df.pivot_table(values='Sprzedaż',index='Region',aggfunc=[len,"max","min"]).round(0))

print("-----------------------data aggregation----------------")