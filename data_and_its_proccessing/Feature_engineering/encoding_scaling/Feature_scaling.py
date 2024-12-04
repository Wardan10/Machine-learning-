# scaling the data to standardize all the features to convinient range
# ex: KNN uses distance between two points and diff between large values makes it inefficient

# standardization and Normalization:
"""
Standardization:

Use when features have different units and ranges.
Suitable for algorithms assuming normally distributed data.
Beneficial for distance-based algorithms and models using gradients.
Ideal for datasets where features vary greatly in magnitude or units.
Normalization:

Use when you want to scale features to a specific range (e.g., [0, 1]).
Suitable for algorithms that do not assume any specific data distribution.
Ideal for neural networks and K-Means clustering.
Beneficial when features have varying scales but need to be compared directly.


->    is feature scaling required?
->    standardised is mostly used
->    if there is fixed boundary then normalisation:



# Standardization(z-score normalization):
Algos that needs standardization for better performance:
    -> K-means
    -> K-nearest neighbours
    -> Principal component Analysis
    -> Artificial Neural Network
    -> Gradient Descent

    New_value = X-mean(X)/
                stand(X)
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

df=pd.read_csv("linear_reg.csv")
scaler=StandardScaler()
scaler.fit(pd.DataFrame(df['age']))   #requires pd.df not series
print(scaler.mean_)
print(df['age'])
X_train=scaler.transform(pd.DataFrame(df['age']))
# both fit and transform can be simplified to fit_transform
print(X_train)
plt.subplot(1,2,1)
plt.hist(df['age'],label='before scaling')
plt.subplot(1,2,2)
plt.hist(X_train,label='after scaling')
plt.show()  # both the plots are goint to be same:
# Normalizaion:
"""
    change the values to a common scale without distorting differnces in the ranges 
    of values of losing information
    
    ->  MinMax scaling
    ->  Mean Normalization
    ->  Robust scaling
"""
# MinMax scaling:
"""
     x=   x-x_min/
        x_max-x_min

"""
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
data=pd.DataFrame(df,columns=['age','bmi'])
scaler.fit(data)
x=pd.DataFrame(scaler.transform(data),columns=data.columns)
# remember scaling transformations return np data 
print(data)
plt.subplot(1,2,1)
plt.scatter(df['age'],df['bmi'],label='before scaling')
plt.subplot(1,2,2)
plt.scatter(x['age'],x['bmi'],label='after scaling')
plt.show()
#  Mean normalization:
"""
    x=   x-x_mean/
        x_max-x_min
"""
# Maxabscaling: (if more zeros then to use this:) 
"""
    x=  x/
      x_max
"""
#robust scaling:
"""
x =      xi-median/
    75thpercentile-25th percentile

-> if the data has outliers these can be useful(robust to outliers)    
"""
