#categorical data encoding:
"""
->nominal(categorize)(ONE HOT ENCODING)
->ordinal(ordered data first,second..)
->labelencoder
ordinal->
    specify the priority to the function
"""
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder,LabelEncoder,OneHotEncoder
df=pd.read_csv('linear_reg.csv')
print(df['sex'].value_counts(),df['sex'])
# currently didn't find ordinal data
#  example encoder=ordinalencoder(categories=[['low','medium','high'],['worst','worser','bad']])

#  label_encoder only the target value not the input value(doubt)
le=LabelEncoder()
df['sex']=le.fit_transform(df['sex'])
print(df['sex'].value_counts(),df['sex'])
#  some algorithms are sensitive to scaling and this can cause invalid outputs


# nominal encoding:(One hot encoding)
# print(df['region'].value_counts())
# # if there are categories whose frquency is low we combine those into one category ->others
# one.fit_transform(pd.DataFrame(df['region']))
# print(df.columns)
# using get_dummies->
one=OneHotEncoder(drop='first',sparse_output=False)  # important!!!!!!!!!!!!!!!!
k=pd.get_dummies(df,columns=['region','sex'],drop_first=True)
print(k)
sparsed_data=one.fit_transform(df[['region','sex']])
print(sparsed_data)



# column transformer->
# simple imputer helps to fill missing values simpleimputer
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
transformer=ColumnTransformer(transformers=[('tnf1',SimpleImputer(),['age','charges','bmi'])
                                            ,('tnf2',OneHotEncoder(drop='first',sparse_output=False),['region','sex'])
                                            ],remainder="passthrough")
x_new=transformer.fit_transform(df[['sex','age','bmi','charges','region']])
print(x_new)

