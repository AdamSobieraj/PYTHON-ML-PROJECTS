import numpy as np
my_arr = np.arange(21)
print("----------------operations--------------------")
print(my_arr)


print("----------------operations slice--------------------")
print(my_arr[5:15])
print(my_arr[5:15:5])

print("----------------operations two dim--------------------")
two_dim = np.array([[0,10,20],[5,15,25],[100,200,300]])
print(two_dim)

print("----------------operations slice--------------------")
print(two_dim[0])
print(two_dim[1][0])
print(two_dim[1:3,:2])

print("----------------fancy indexing--------------------")
my_arr = np.arange(25).reshape(5,5)
print(my_arr)

print("----------------operations slice--------------------")
print(my_arr[(0,1)])
print(my_arr[(0,1),])
print(my_arr[[0,1],[0,4]])

print("----------------operations vector--------------------")
vals = np.array([100,5,0])
select = np.random.randint(0,3,size=(4,3))
print(select)

print("----------------operations--------------------")
print(vals[select])
print(vals[[1,0,2]])

print("----------------operations slicing--------------------")
arr = np.arange(10)
print(arr)

slice_of_arr = arr[:5]
print(slice_of_arr)

slice_of_arr[:] = 100
print(slice_of_arr)

print(arr)

print("----------------operations fancy index--------------------")
fancy_arr = np.arange(10)
print(fancy_arr)

fancy_index_arr = fancy_arr[np.arange(5)]
print(fancy_index_arr)

fancy_index_arr[:] = 100
print(fancy_index_arr)

print(fancy_arr)

print("----------------operations checking type--------------------")
print(slice_of_arr.base is None)

print(fancy_index_arr.base is None)

print(slice_of_arr.base is arr)

print("----------------operations copy--------------------")
arr = np.arange(10)
print('arr')
print(arr)

slice_of_arr = arr[:5].copy()
print('slice_of_arr')
print(slice_of_arr)

slice_of_arr[:] = 100
print('slice_of_arr')
print(slice_of_arr)

print('arr')
print(arr)

print(slice_of_arr is arr)

print("----------------operations matrix example--------------------")
macierz = np.arange(9).reshape(3, 3)
print(macierz)
macierz[-1, -1] = 999
macierz[1:, 1:] = 0
print('\n', macierz)

print("----------------operations--------------------")
#Znajdź indeksy niezerowych elementów z tablicy array([1,2,0,0,4,0]).


print("----------------operations masking--------------------")
arr = np.arange(0,50,5)
print(arr)

print("----------------operations filter matrix--------------------")
print(arr>15) # chcek field values
print(arr[arr>15])

print((arr>15) & (arr!=40))
print(arr[(arr>15) & (arr!=40)])

print(np.logical_or(arr<10,arr>=20))
print(arr[np.logical_or(arr<10,arr>=20)])

print(np.where(arr<=43))

#Wyfiltruj z arr tylko te wartości, które są mniejsze od 10 lub większe bądź równe 20, ale jednocześnie różne od liczby 40. (gdzie arr = np.arange(0,50,5)).
#Wykorzystując operator XOR, stwórz macierz o kształcie (4,4), której elementy po głównej przekątnej mają wartość logiczną False, a pozostałe wartość True.

print("----------------Mix – indexing, slicing oraz masking--------------------")
arr = np.arange(20).reshape(4,5)
print(arr)

print(arr[[3,0,1],:3])

print(arr.sum())

print(arr[arr.sum(axis=1)>10,2:])


# print("----------------operations--------------------")
# Zwróć z macierzy arr wiersz o indeksie nr 2, lecz tylko dla tych kolumn, których suma przekracza 30.
# Mamy dane dwie tablice: a i b. Stwórz program filtrujący wartości z b, które korespondują z elementami a i są większe od 100 i mniejsze od 110.
# a = np.array([97,101,105,111,117,125])
# b = np.array(['a','e','i','o','u','y'])
# Stwórz program, który ze wskazanej macierzy wyciągnie odpowiednio najmniejszą i największą wartość dla każdego wiersza.
# [[0 4 1]
# [2 0 4]]
# Mając tablicę np.arange(11), odwróć znak wszystkich elementów większych od 3 i mniejszych od 8.

print("----------------Operacje na macierzach--------------------")
macierz_1 = np.array([[1,3,6],
                      [7,1,1],
                      [7,2,7]])

print(f'Macierz 1\n{macierz_1}')
macierz_2 = np.array([[-9,3,7],
                      [7,3,1],
                      [-1,-9,5]])

print(f'Macierz 2\n{macierz_2}')

print(macierz_1 + macierz_2)

print(np.add(macierz_1, macierz_2))

print(macierz_1 - macierz_2)

print(np.subtract(macierz_1, macierz_2))

# Wartości macierzy możemy mnożyć przez skalar lub przez wartości w innej macierzy.
print(macierz_1 * 10)
print()
print(macierz_1 * macierz_2)

print(macierz_1.dot(macierz_2))

print("----------------operations--------------------")
arr = np.arange(0,101,10)
print(arr)

print(arr + arr)

print(arr * arr)

# przez skalar
print(arr + 5)

print(arr / 5)

left_ = np.arange(10).reshape(5,2)
right_ = np.arange(5).reshape(5,1)

print(left_)
print(right_)


print("----------------operations npy operations--------------------")
arr = np.arange(0,101,10)

print(arr)
print(np.sqrt(arr))
print(np.sin(arr))
print(np.multiply(arr,2))

#
# Stwórz program, który ze wskazanej macierzy wyciągnie odpowiednio najmniejszą i największą wartość dla każdego wiersza.
# [[0 4 1]
# [2 0 4]]
# Stwórz wektor Z według następującego wzoru: np.random.uniform(0,1,10). Następnie znajdź element, który jest najbliższy wartości 0.5.
# Stwórz wektor zawierający 20 losowych wartości, a następnie zamień jego największą wartość na 0.
# Znajdź części całkowite tablicy, wykorzystując przynajmniej dwa różne sposoby.
# np.array([5, 0.0249139 , 0.11873564, 0., 0.72321586, 11308494, 0.29931472, 0.24439968, 0.61251754, 4])


print("----------------Gregation ndarray--------------------")
print(arr)

print(arr.sum())

print(arr.mean())

print(arr.min())

print(arr.max())

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d, '\n')
print(arr_2d.min(axis=0), '\n')
print(arr_2d.min(axis=1))

# W podobny sposób możesz policzyć medianę (np.median), wariancję (np.var) czy odchylenie standardowe (np.std).

arr = np.arange(0,101,10)
print(arr)


print("----------------Sortowanie--------------------")

arr = np.random.randint(1,40,10)
print(arr)

print(np.sort(arr))
# Pamiętaj jednak, że nie wprowadziliśmy zmiany dla Twojego wektora (otrzymujesz jedynie kopię). Musisz nadpisać zmienną arr, aby zachować posortowane wartości.

print(arr)
np.sort(arr)
print(arr)
arr = np.sort(arr)
print(arr)

arr = np.sort(arr)[::-1]
print(arr)

print(arr)
arr.sort()
print(arr)

# określamy oś sortowania
arr2d = np.array([np.arange(1,6),np.arange(6,1,-1)]).reshape(5,2)
print(arr2d)

print(np.sort(arr2d))

print(np.sort(arr2d,axis=0))

print("----------------Structured Array--------------------")
dt = np.dtype([('student','S10'),('exam1',int),('exam2',int)])

a = np.array([("Student A",89,74),("Student B",85,56),
              ("Student C", 93,44), ("Student D",83,92)],dtype=dt)

print(a)

print(np.sort(a,order='exam1'))

print(np.sort(a,order='exam2'))

print(np.sort(a,order='exam2')[-1][0])

print(arr)

print(np.argsort(arr))

print("----------------operations--------------------")
