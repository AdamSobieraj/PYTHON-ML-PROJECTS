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

print("----------------operations--------------------")
print("----------------operations--------------------")