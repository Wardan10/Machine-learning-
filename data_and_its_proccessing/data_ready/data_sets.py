import matplotlib.pyplot as plt
import  sklearn.datasets as ds

#sklearn data sets->
x,y=ds.make_classification(n_features=2,n_samples=1000,n_repeated=0,n_informative=2,n_clusters_per_class=1,n_redundant=0)

from matplotlib import style
print(x.shape)
# plt.scatter(x[:,0],x[:,1],y)
plt.scatter(x[:, 0], x[:, 1], c=y, cmap='viridis', edgecolor='k')
plt.scatter()
plt.show()
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.05)
model.fit(x_train,y_train)
result=model.predict(x_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(result,y_test))


# retriving data->
"""
 • Popular open data repositories:
 —UC Irvine Machine Learning Repository
 —Kaggle datasets
 —Amazon AWS datasets
 
 
 • Meta portals (they list open data repositories):
 —http://dataportals.org/
 —http://opendatamonitor.eu/
 —http://quandl.com/
 
 
 • Other pages listing many popular open data repositories:
 —Wikipedia list of Machine Learning datasets
 —Quora.com question
 —Datasets subreddit
"""
