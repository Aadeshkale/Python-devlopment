import numpy as np
import pandas as pd

# DataFrame with perticular data
l=['mango','orange','graphes','apple']
df=pd.DataFrame(l)
print(df)
# DataFrame wit custom indexes

df=pd.DataFrame(l,['a','b','c','d'],["fruits"])
print("\n",df)
print()

#DataFrame with matrix array

df=pd.DataFrame(np.arange(1,31).reshape(5,6),[1,2,3,4,5],['a','b','c','d','e','f'])
print(df)

print("Accessing cols element:\n",df['c'])
print(type(df['c']))
print("Acessing mutiple cols:\n",df[['a','b','c']])

# Adding new col
df['new']=df['a']+df['b']
print(df)
print()
#drop col opration
print(df.drop('new',axis=1))

# drop permanentely
print(df)
print()
df.drop('new',axis=1,inplace=True)
print(df)


#  accessing rows
print(df.loc[4])
print()
print(df.loc[[3,4,5]])

# drop rows
print(df.drop(5))
print()
# permanently drop row
print(df)
print()
df.drop(5,inplace=True)
print(df)
print()
print(df)
print()
#subset of Dataframe
print(df.loc[[2,3,4],['a','b','c']])
