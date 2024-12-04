#we can operate np operations on dataframes and series
import pandas as pd
import numpy as np
x=pd.DataFrame(abs(np.random.randn(4,2)),columns=["alice","bob"])
print(x)
print(np.average(x))
print(x+(1,2))
#and also pd operations:

