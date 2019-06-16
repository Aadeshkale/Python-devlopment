import  numpy as np
import pandas as pd

# reletional oprations

df=pd.DataFrame(np.random.randn(5,6),['a','b','c','d','e'],['u','v','w','x','y','z'])
print(df)
print("relational oprations")
print()
print(df>0) # return true-false dataFrame
print()
print(df[df>0]) # retrn DataFarme with NaN values
print()
print(df[df['u']>0]) # retrrn all the value greatrher than 0 with other cols
print()
res=df[df['u']>0]
print(res[['x','y','z']])
print()
print(df[df['u']>0][['x','y','z']])
print("logical oprators")
print((df[df['u']>0]) | (df[df['v']>0])) # values are generated randomly so it may give error some times
print(df)