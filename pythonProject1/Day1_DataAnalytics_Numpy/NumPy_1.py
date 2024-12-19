import numpy as np
arr = np.array([1,2,3,4])
Scalar = 7
result = arr + Scalar
print(result)

#array from list
list=[1,2,3,4]
list_arr=np.array(list)
print(list_arr)

#from in-built functions
print(np.arange(1,10))
print(np.arange(1,10,2))
print(np.zeros((3,3)))
print(np.ones((3,3)))
#from list of list
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(np.array(matrix))

#from linespace
print(np.linspace(2,3))
print(np.linspace(2,5,10))

#random arrays
print(np.random.rand(2))
print(np.random.rand(5,5))

#random arrays for normal distribution
print(np.random.randn(2))
print(np.random.randn(5,8))

#random integers for a range of values
print(np.random.randint(1,100)) #single integer from range
print(np.random.randint(1,100,10)) #10 random integers

#seeding for reproducable results
np.random.seed(77)
print(np.random.rand(4))

#storing
arr = np.arange(25)
ranarr = np.random.randint(0,50,10)
print(arr, ranarr)

#reshape
print(arr.reshape(5,5))