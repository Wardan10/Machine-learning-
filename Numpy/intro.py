import numpy as np
#numpy mainly deals with array processing which provides 
#functions to work with n dimensional arrays
#provides powerful array objects that are efficient and felxible
#number of dimensions is called ' RANK ' of the array
#tuple which denotes the dimensions of the arrat is called ' shape '\
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr)
initial= np.array([[1, 2, 0,-4],
                [4,-0.5,6, 0],
                [-2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
sliced=initial[:2,::2] #first index signifies rows and how it got slicied,
# second is the colomn slicing
print(initial)
print(sliced)
print(initial.sum())
print(initial+10)
sliced[0][0]=1000
print("Initial->")
print(initial)
# type casting->
x=np.array([10.5,11,15.5],dtype=np.int32)
y=np.array([10.5,11,15.5],dtype=np.float32)
print(x,x.dtype)
print(y,y.dtype)
z=sliced.T # Transpose of the matrix
print(z)
print(np.sqrt(z))
x=np.arange(0,8).reshape(2,4)
print(x,x.prod())