import numpy as np
# merging two arrays ->
p=np.array([[1,2],[3,4]])
q=np.array([[5,6],[7,8]])
print(np.vstack((p,q)))
print(np.hstack((p,q)))
x,t=np.hsplit(p,2).copy() # number of divisions
print(x,t)
#concatenation->
print(np.concatenate((p,q),axis=None))#none falttens the arrays
print(np.concatenate((p,q),axis=0))#along rows
# misc functions->
a=np.array([[1,2,3,4],[5,6,7,8]])
for funcs in a.sum,a.min,a.max,a.__abs__:
    print(funcs.__name__,funcs())

print(p.max(axis=0),p.max(axis=1))

# np.unique
something=np.arange(0,6).reshape(2,3)
print(something)
print("matrix ,counts:\n",np.unique(something,return_counts=True))# frequncy by retu..
############generating random nums->
print(np.random.rand(1,6))# only +ve values
print(np.random.randn(3,4)*100)
# tanspose,flip->
print(np.transpose(something))
print(np.flip(something))  # reverse the array->
#flatten->
print(something.flatten())
# ravel->to make a new array with the refernce to an array 
somethin1=something.ravel()
somethin1[3]=100
print(something)
print(np.linspace(0,3,10))