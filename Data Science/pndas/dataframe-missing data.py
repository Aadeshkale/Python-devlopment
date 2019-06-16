import numpy as np
import pandas as pd
d={ 'a':[1,2,np.nan],
    'b':[2,np.nan,np.nan],
    'c':[1,2,3]
    }
df=pd.DataFrame(d)
print(df)
print()
# removeing all nan nan values form rows
res=df.dropna()
print(res)
print()
# removeing all null values form cols
res=df.dropna(axis=1)
print(res)
print()
# removing values with thresh for rows
res=df.dropna(thresh=2)
print(res)
print()
#removeing values with thersh for cols
res=df.dropna(axis=1,thresh=2)
print(res)
print()
# filling nan with perticular value
res=df.fillna(value="ok")
print(res)
print()
# filling an mean value
res=df[['a','b','c']].fillna(value=df[['a','b','c']].mean())
print(res)
