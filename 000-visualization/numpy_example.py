import numpy as np

print("---------------------base element Numpy------------------------")
exams = np.asarray([[100, 200, 50, 400], [50, 0, 0, 100], [350, 100, 50, 200]])
print(exams)

print("---------------------parametry Numpy------------------------")
one_dim = np.array([1,2,3,4])

print(one_dim)
print(type(one_dim))

print(one_dim.shape) # kształt

print(one_dim.ndim) # liczba wymiarów – w tym przypadku 1 wymiar


print("---------------------reshape element Numpy------------------------")

one_dim_horizontal = np.array([[1,2,3,4]])
print(one_dim_horizontal.shape)
print(one_dim_horizontal)

one_dim_vertical = one_dim_horizontal.reshape(-1, 1)
print(one_dim_vertical)

print(one_dim_vertical.reshape(1, -1))
print(one_dim_vertical)

print("---------------------reshape 2n element Numpy------------------------")
two_dim = np.array([[100, 200, 50, 400], [50, 0, 0, 100], [350, 100, 50, 200]])

print(two_dim)
print("len: " + str(len(two_dim)))
print("shape: " + str(two_dim.shape))
print("ndim: " + str(two_dim.ndim))

print("Size : {}".format(two_dim.size))
print("Element size : {}".format(two_dim.itemsize))

print("One dim reshape : {}".format(one_dim.reshape(2,2)))
print("Two dim reshape : {}".format(two_dim.reshape(4,3)))

print("Two dim to array : {}".format(two_dim.flatten()))

print("---------------------matrix generate Numpy------------------------")
print(np.zeros((5,3)))
print(np.ones((2,3),dtype=np.int8))

arr_01 = np.array([5, 10, 20])
print(arr_01, arr_01.dtype)
arr_02 = np.array([5, 10, 20.0])
print(arr_02, arr_02.dtype)
arr_03 = np.array([5, 10, '20'])
print(arr_03, arr_03.dtype)

print("Linspace {}".format(np.linspace(0,5,10)))
print("eye {}".format(np.eye(4)))
print("diag".format(np.diag([5, 0, 4, 1, 3, 2])))
print("".format())

print("---------------------base element Numpy------------------------")