import numpy as np
import pandas as pd

d1={
    'company':['google','google','oracle','oracle','msoft','msoft'],
    'person':['a','b','c','d','e','f'],
    'sales':[10,20,30,40,50,60]
}

df1=pd.DataFrame(d1)
print(df1)

# groupby
res=df1.groupby('company').mean()
print(res)
print()
# describe provides agrigation funtions like min,max,count,std..etc

res=df1.groupby('company').describe()
print(res)

