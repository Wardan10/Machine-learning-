"""
pipelines chains together multiple steps so that the output 
of each step is used as input to the next step
pipelines makes it easy to apply the same preproccessing to train and test!

"""
#  with no pipeline ->
import pandas as pd
from sklearn.impute  import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,LabelEncoder,OrdinalEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier
df=pd.read_csv('titanic.csv')
print(df.head())
df.drop(columns=['PassengerId','Name','Ticket','Cabin'],inplace=True)
print(df.isna().sum())
# age-> 117 missing
mode=df['Age'].mode().iloc[0]
df['Age']=df['Age'].fillna(mode)
mode=df['Embarked'].mode().iloc[0]
df['Embarked']=df['Embarked'].fillna(mode)
print(df.isna().sum())

#Categorical data encoding:
ohe_sex=OneHotEncoder(sparse=False)
ohe_embarked=OneHotEncoder(sparse=False)
x_new_sex=ohe_sex.fit_transform(df['Sex'])
x_new_embarked=ohe_embarked.fit_transform(df['Embarked'])


x_train,x_test,y_train,y_test=train_test_split(df.drop(columns=['Survived']),df['Survived'],test_size=0.2,random_state=42)
#     BLAH BLAH BLAH

