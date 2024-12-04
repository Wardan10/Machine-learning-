import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
my_birtdays=pd.date_range(start='2005/06/10 5:45',end='2024/10/10 5:45',freq='YE')#only three must be specified periods or freq
print(my_birtdays,"\n",my_birtdays.to_period())
#skipped time series periods
#dataframes:multiple series in one dictionary each refereing to a particular colomn
x={"first":pd.Series([1,2,3],index=["one","two","three"]),"second":pd.Series([4,5,6],index=["one","two","three"])}
k=pd.DataFrame(x)
print(k)
#retain order:
y=pd.DataFrame(x,columns=["second","first"],index=["three","two","one"])
print(y)
#just pass lists line wise and then difine colowns and indices:
values = [
            [1985, np.nan, "Biking",   68],
            [1984, 3,      "Dancing",  83],
            [1992, 0,      np.nan,    112]
         ]
d3 = pd.DataFrame(
        values,
        columns=["birthyear", "children", "hobby", "weight"],
        index=["alice", "bob", "charles"]
     )
print(d3)
d4=d3.copy()
d4["age"]=2024-d4["birthyear"]
d4.insert(1,"extra",[1,2,3])
print(d4)
#querying:
print(d4.query("age>=40"))
#sort->index and values
print(d4.sort_index(ascending=False))
print(d4.sort_values("age"))
print(d4)#but the dataframe doesn't change ,so make inplace=True
d4.sort_values("age",inplace=True)
print(d4)
#multi_indexing:
d5=pd.DataFrame({("extra_level","1"):{"first":1,"second":2},("extra_level","2"):{"first":3,"second":4}})
print(d5)
d5.columns=d5.columns.droplevel(level=0)
print(d5)
students=pd.DataFrame([[1,2,3],[4,5,6]],index=["first","second"],columns=["x","y","z"])
print(students)
print(students.loc["first"])
print(students.iloc[1])
del students["x"]
print(students)