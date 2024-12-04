import numpy as np
# load,save->deal with .npy binary files
# single arra object we can use npy
# loadtxt,savetxt-> txt files
# multiple .npz is preffered
# we can also use savez.compressed
# leadz,savez ->npz files
a=np.arange(0,6).reshape(2,3)
np.save('a.npy',a)
b=np.load('a.npy')
print(b)
np.savetxt('a_.csv',a)  # we can use txt ans .csv(comma seperated values)
# we can also include header and footer in savetxt
print(np.loadtxt('a_.csv'))
import pandas as pd
x=pd.read_csv('a_.csv',)
print(x)

