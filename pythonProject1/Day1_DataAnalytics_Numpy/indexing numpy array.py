import numpy as np


arr=np.arange(0,11)
print(arr,"\n")

#Bracket indexing
print(arr[8],"\n")

#get values in a range
print(arr[1:5],"\n")

#get values in a range
print(arr[0:5],"\n")

#broadcasting
arr=np.arange(1,11)
slice= arr[0:5]
slice[:]=100
print(slice)
print(arr,"\n")

#Conditioning in array
print(arr>10,"\n")
bool_arr=arr>10

print(arr[bool_arr])

#array arithematics
print(arr+arr,"\n")
print(arr*arr,"\n")
print(arr-arr,"\n")
print(arr/arr,"\n")
print(arr**3,"\n")
# print(arr/0,"\n")

#Universal functions
print(np.sqrt(arr))
print(np.exp(arr))
print(np.sin(arr))
print(np.log(arr))

#summary statistics
print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.min())
print(arr.var())
print(arr.std())

#2D arrays
arr_2d=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr_2d)

#Assignments

print()