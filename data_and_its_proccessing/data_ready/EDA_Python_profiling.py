import pandas as pd
# from pandas_profiling import ProfileReport  requires 3.10 version or below of py 
df=pd.read_csv('linear_reg.csv')
prof=ProfileReport(df)
prof.to_file(output_file='output.html')
