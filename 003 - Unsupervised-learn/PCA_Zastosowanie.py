import numpy as np
import pandas as pd
import seaborn as sns

from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

iris = sns.load_dataset('iris')
print(iris)

print(iris['species'].value_counts())

fig = plt.figure(figsize=(13, 13))
ax = fig.add_subplot(111, projection='3d')
img = ax.scatter(xs=iris.loc[iris['species']=='virginica','sepal_length'],ys=iris.loc[iris['species']=='virginica','sepal_width'],zs=iris.loc[iris['species']=='virginica','petal_length'],s=iris.loc[iris['species']=='virginica','petal_width']*50,c='red', label='virginica')
img = ax.scatter(xs=iris.loc[iris['species']=='setosa','sepal_length'],ys=iris.loc[iris['species']=='setosa','sepal_width'],zs=iris.loc[iris['species']=='setosa','petal_length'],s=iris.loc[iris['species']=='setosa','petal_width']*50,c='green', label='setosa')
img = ax.scatter(xs=iris.loc[iris['species']=='versicolor','sepal_length'],ys=iris.loc[iris['species']=='versicolor','sepal_width'],zs=iris.loc[iris['species']=='versicolor','petal_length'],s=iris.loc[iris['species']=='versicolor','petal_width']*50,c='blue', label='versicolor')
ax.set_xlabel(xlabel='sepal length', size=15)
ax.set_ylabel(ylabel='sepal width', size=15)
ax.set_zlabel(zlabel='petal length', size=15)
ax.set_title('Rozmiar punktu: petal width', size=15)
plt.legend(title='Species')
plt.show()

sns.pairplot(iris,hue='species',palette={'virginica': 'red', 'setosa': 'green','versicolor': 'blue'})
plt.show()

# korelację Pearsona:

# plt.figure(figsize=(12, 12))
# ax = sns.heatmap(iris.corr(),xticklabels=iris.corr().columns,yticklabels=iris.corr().columns,cmap='RdYlGn',center=0,annot=True,vmin=-1,vmax= 1)4 plt.title('Korelacja dla zmiennych z IRIS', fontsize=24)
# bottom, top = ax.get_ylim()
# ax.set_ylim(bottom + 0.5, top - 0.5)
# plt.xticks(fontsize=15)
# plt.yticks(fontsize=15)
# plt.show()


X = iris.drop('species', axis=1).copy()
y = iris['species'].copy()
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.5, random_state=42, stratify=y)
scaler = StandardScaler()
X_train_scaler = scaler.fit_transform(X_train)
pca = PCA(random_state=42)
X_train_pca = pca.fit_transform(X_train_scaler)
train_iris =pd.DataFrame(np.concatenate([X_train_pca,np.array(y_train).reshape(-1,1)],axis=1))
train_iris.rename(columns = {0: 'PC1', 1:'PC2',2: 'PC3', 3: 'PC4', 4:'species'},inplace=True)
train_iris[['PC1', 'PC2','PC3','PC4']] = train_iris[['PC1','PC2','PC3', 'PC4']].astype(float)
train_iris.corr()

fig, ax = plt.subplots(figsize=(12, 12))
plt.imshow(pca.components_.T, cmap = 'Spectral', vmin =-1, vmax =1)
plt.yticks(range(len(X_train.columns)), X_train.columns,fontsize=12)
plt.xticks(range(4), range(1, 5), fontsize=12)
plt.xlabel('Główne Składowe', fontsize=15)
plt.ylabel('Zmienne', fontsize=15)
plt.title('Rozkład zmiennych według głównych składowych ~ PCA',
fontsize=20)
plt.colorbar()
plt.show()

# wykres skumulowany.
fig = plt.figure(figsize=(12,8))
fig.subplots_adjust(wspace=.4, hspace=.4)
ax = fig.add_subplot(2, 1, 1)
ax.bar(range(1, 1+pca.n_components_),pca.explained_variance_ratio_, color='black')
ax.set(xticks=[1, 2, 3, 4])
plt.yticks(np.arange(0, 1.1, 0.1))
plt.title('Wyja?niona wariancja', fontsize=15)
plt.xlabel('G?ówne Sk?adowe', fontsize=13)
plt.ylabel('% wyja?nionej wariancji', fontsize=13)
ax = fig.add_subplot(2, 1, 2)
ax.bar(range(1, 1+pca.n_components_),
np.cumsum(pca.explained_variance_ratio_), color='black')
ax.set(xticks=[1, 2, 3, 4])
plt.yticks(np.arange(0, 1.1, 0.1))
plt.title('Skumulowanana Wyja?niona wariancja', fontsize=15)
plt.xlabel('G?ówne Sk?adowe', fontsize=13)
plt.ylabel('% wyja?nionej wariancji', fontsize=13)
plt.show()
principal_component = 1
cum_explained_var = 0
for explained_var in pca.explained_variance_ratio_:
    cum_explained_var += explained_var
print(f'G?ówna sk?adowa: {principal_component}, Wyja?niona wariancja: {np.round(explained_var, 5)}, Skumulowana Wyja?niona wariancja: {np.round(cum_explained_var, 5)}')
principal_component += 1

fig = plt.figure(figsize=(12, 12))
plt.scatter(x=train_iris.loc[train_iris['species']=='virginica','PC1'],y=train_iris.loc[train_iris['species']=='virginica','PC2'],c='red', label='virginica', s=50)
plt.scatter(x=train_iris.loc[train_iris['species']=='setosa','PC1'],y=train_iris.loc[train_iris['species']=='setosa','PC2'],c='green', label='setosa', s=50)
plt.scatter(x=train_iris.loc[train_iris['species']=='versicolor','PC1'],y=train_iris.loc[train_iris['species']=='versicolor','PC2'],c='blue', label='versicolor', s=50)
plt.xlabel(xlabel='PC1', size=15)
plt.ylabel(ylabel='PC2', size=15)
plt.title('Wykres G?ównych Sk?adowych', size=20)
plt.legend(title='Species')
plt.show()