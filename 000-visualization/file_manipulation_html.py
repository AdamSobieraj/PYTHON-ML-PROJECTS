import pandas as pd

data = pd.read_html('https://pl.wikipedia.org/wiki/Miasta_w_Polsce', header=0)

print("-------------------data check------------------------")
type(data)

print("-------------------data -----------------------------")
print(data[0])

print("-------------------data end------------------------")