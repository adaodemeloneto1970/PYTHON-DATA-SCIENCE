import numpy as np
import sys

a=[1,2,3,4,5]

b= np.array([1,2,3,4,5])

print(a)

print(b)

print(sys.getsizeof(a))

print(sys.getsizeof(b))

d1= np.array([1,2,3])
print(d1)
print(d1.ndim)

d2= np.array([[1,2,3],[4,5,6]])
print(d2)

print(d2.ndim)

d3= np.array([[[1,2],[4,5]],[[4,5],[2,4]]])
print(d3)

print(d3.ndim)

a=[2,3,4]
b=[2,3,4]

result= a+b
print(result)

a= np.array([2,3,4])
b= np.array([2,3,4])

result=np.add(a,b)

print(result)

a= np.array([[2,3,4,5],[6,7,8,9]])

print(a)

print(a[1,2])
print(a[0,:])
print(a[:,1])











