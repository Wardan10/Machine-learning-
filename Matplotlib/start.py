import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
print(mpl.get_backend()) #currently using TkAgg agg->anti-grain geometry engine
x=np.linspace(-1,1,100)
y=x**2
Y=x**3
plt.title('Y=X^2 and X^3 ')
plt.xlabel('x->')
plt.ylabel('y->')
plt.plot(x,y,label='y=x^2')
plt.plot(x,Y,label='y=x^3')
# plt.legend(['y=x^2','y=x^3'])  or we can specify the lables bear the plots
plt.legend()
plt.show()
plt.close()
fig = plt.figure()  # an empty figure with no Axes
                        #######start#######
# an axes is one individual plot, axes is the class with all the functionalities to plot
 
# axis is dimensions

# artist is the interface which includes all the things we see on a plot

# # to plot a graph in matplotlib we need to convert the array like data type to asarray type using np midule

# the oop method , maually exptrating axes and manipulating it 
fig, ax=plt.subplots(figsize=(7,7),layout='constrained')
ax.plot([1,2,3],[1,2,3],label='linear')
plt.show()
plt.close()
# using plt -> normal usage as first
# default x points are the indices
################  markers->

plt.plot([2,3,12,34,23,1,34,26,53,112],marker='o')
# colors ,lines and  markers refernce https://www.w3schools.com/python/matplotlib_markers.asp
plt.plot(np.concatenate((np.linspace(-5,0,5),np.linspace(0,-5,5)),axis=None),marker='v',ms=5,mfc='r')
plt.show()
plt.close()
########## lienstyle ->
#ref->https://www.w3schools.com/python/matplotlib_line.asp
plt.plot([1,2,3,4],[1,2,3,4],ls='dotted',c='g',linewidth=5)
plt.show()