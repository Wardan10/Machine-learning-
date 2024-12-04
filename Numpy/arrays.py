#adding size
import numpy as np
a=np.array([1,2,3,5,6,6])
print(a.shape)
row=a[np.newaxis,:]   #newaxis increases the dimen by one
print(row,row.shape)
row=row[np.newaxis,:]
print(row,row.shape)
col=a[:,np.newaxis]
print("New dimension")
print(col,col.shape)
b=np.expand_dims(a,axis=1) #adds new dimension to the array at the specified index
print(b,b.shape)
c=np.expand_dims(a,axis=0).copy() # moves a to index 1 that is col coordinate and new dimension in rows
print(c,c.shape)
b=np.expand_dims(b,axis=1)
print(b,b.shape)
# important if we modify any array which is from a parent array,changes to children array changes the parent array
b[5][0][0]=1000
print(a)
# but
c[0][5]=99
print(a) # this doesn't chnage a becuase c=a.copy()
a=np.array([[1,2,3,4],[5,6,7,8]])
print(a[a%2==0])
# to find the indices use nonzero()
print(np.nonzero(a%2==0))


