# what the hell
# without pipeline # ignored
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,MinMaxScaler
from sklearn.pipeline import Pipeline,make_pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_selection import SelectKBest,chi2
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
df=pd.read_csv('titanic.csv')
# create a pipeline 
df.drop(columns=['PassengerId','Name','Ticket','Cabin'],inplace=True)
X_train,X_test,Y_train,Y_test=train_test_split(df.drop(columns=['Survived']),df['Survived'],test_size=0.2,random_state=42)
# FIRST -> Fill Na
transformer_1=ColumnTransformer([
    ('impute_Age',SimpleImputer(),[2]),  # for pipelines it's better to call by index
    ('impute_embarked',SimpleImputer(strategy='most_frequent'),[6])],remainder='passthrough'
)
#  handle_unknown -> imp doubt more!!
transformer_2=ColumnTransformer([
    ('ohe',OneHotEncoder(sparse_output=False,handle_unknown='ignore'),[1,6])
],remainder='passthrough')
transformer_3=ColumnTransformer([
    ('scale',MinMaxScaler(),slice(0,10)) # for feature selection
])
transformer_4=SelectKBest(score_func=chi2,k=8)
transformer_5=DecisionTreeClassifier()
# pipe=Pipeline([('1',transformer_1),('2',transformer_2),('3',transformer_3),('4',transformer_4),('5',transformer_5)])
# #  orr simple one-> without names
pipe1=make_pipeline(transformer_1,transformer_2,transformer_3,transformer_4,transformer_5)
from sklearn import set_config
# pipe1 -> display's total pipeline in jupyter lab
# result=pipe1.transform(X_test)
pipe1.fit(X_train,Y_train)
set_config(display='diagram')
from sklearn.metrics import accuracy_score
# print(accuracy_score(pipe1.predict(X_test),Y_test))
print(Y_test)
res=pipe1.predict(X_test)
print(res)

