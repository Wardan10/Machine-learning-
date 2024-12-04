#pandas is a powerful and opensrc lib for data manip and analysis
#built on top of numpy

# mainly deals with the data in tabular form called dataframe
#-> datset cleaning,merging and joining
# reading ,writing to ,from CSV,XLS,HTML,SQL,JSON..
# plotting
# statistics
# deal with times series too!
import pandas as pd
import numpy as np
#  SERIES
s1=pd.Series([1,2,3,4])
s=pd.Series([3,2,12,4],index=["one","two","Three","four"])
print(s,"\n",s["Three"],s[2]) #may generate warning 
#-> use loc for dict and iloc for list type accessing
print(s.loc["four"],s.iloc[3])
#init through dicts=>
weights = {"alice": 68, "bob": 83, "colin": 86, "darwin": 68}
s3 = pd.Series(weights)
print(s3)
#control the inputs by indices
# s4=pd.series(weights,index=["alice","bob"])
# print(s4)
init_with_scalar=pd.Series(100,["garsasd","dasdwa"])
print(init_with_scalar)

#series can have a name-> 
named_series=pd.Series([121,12312,123],index=["harssha","wardan","siraboina"],name="Name")
import matplotlib.pyplot as plt
plt.plot(named_series)
plt.show()


