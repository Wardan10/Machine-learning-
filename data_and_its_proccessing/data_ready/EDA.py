# analyse the shape and use head() or sample() to get the basic idea of the data
# data_type of all the cols
import pandas as pd
data=pd.read_csv("linear_reg.csv")
print(data.shape)
print(data.head(),data.info())
# print(data.isnull().sum())
# do fill na data
data.describe() # math representation
# duplicate values->
print("duplicates:\n",data.duplicated())

#correlation:

# print(data.corr()) make sure all the vals are numerical

#             Exploratory Data analysis:(Vizualization)
#   Univariate analysis:
#   -> data:numerical or categorial
#   -> perform UE on each column
import matplotlib.pyplot as plt
# features-> age,sex,bmi,children,smoker,region,charges
df=data.copy()    # filter useful data:


# df.drop(columns=['region','smoker','sex'])
# def func(x):
#     if x=="northeast":return 1
#     if x=="northwest":return 2
#     if x=="southeast":return 3
#     if x=="southwest":return 4
# df['region']=data['region'].apply(func)
# df['sex']=data['sex'].apply(lambda x:1 if x=="male" else 0)
# df['smoker']=data['smoker'].apply(lambda x:1 if x=="yes" else 0)
#### best way->
import pandas as pd
df=pd.read_csv("linear_reg.csv")
from sklearn.preprocessing import LabelEncoder # or labelbinarizer
le=LabelEncoder()
for cols in df.select_dtypes(include='object').columns:
    df[cols]=le.fit_transform(df[cols])
print(df.head())
print(df.corr())

# charges is in close correlation with age , bmi and smoking
plt.subplot(2,2,1)
plt.hist(df['sex'],label="sex")
plt.subplot(2,2,2)
plt.hist(df['smoker'],label="smokers")
plt.subplot(2,2,3)
plt.hist(df['region'],label="region")
plt.subplot(2,2,4)
plt.hist(df['children'],label="children")
plt.show()
plt.close()
# numerical data:
plt.hist(df['age'],bins=20)
plt.show()


##                                  BOXPLOT                       ##
# box ->left boundary 25 % mark(Q1) , right boundary 75%(Q3) 
# left and right line(min and max (not really))->    (Q1-1.5(Q3-Q1)) ,  (Q3-1.2(Q3-Q1))
# others are outliners
df=df.drop(columns=['children','region'])
plt.boxplot(df['age'])
plt.show()

                        #  Multivariate analysis:
import seaborn as sns
#scatterplot:
plt.scatter(df['age'],data['charges'],c=df['sex'])
plt.show()
    # pairplot:
sns.pairplot(df,height=1,aspect=1,hue='sex')
plt.show()