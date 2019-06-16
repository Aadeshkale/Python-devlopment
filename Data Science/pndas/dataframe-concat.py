import numpy as np
import pandas as pd
d1=np.arange(1,7).reshape(3,2)
d2=np.arange(6,12).reshape(3,2)

df1=pd.DataFrame(d1,[1,2,3],['a','b'])
df2=pd.DataFrame(d2,[1,2,3],['a','b'])
print(df1)
print()
print(df2)
print()
# concatanation with rows
res=pd.concat([df1,df2])
print(res)
print()
# concatnation with cols
res=pd.concat([df1,df2],axis=1)
print(res)