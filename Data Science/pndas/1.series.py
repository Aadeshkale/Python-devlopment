
import pandas

l=[112,12,64]
t=(1,1,2)
d={'k1':121,'k2':12356}

# creating series

sl=pandas.Series(l)
st=pandas.Series(t)
sd=pandas.Series(d)
print("Sreies of list:\n",sl)
print("Sreies of tuple:\n",st)
print("Sreies of directory:",sd)

# series with coustmize index
label=['a','b','c']
sl=pandas.Series(l,label)
print("series list with coustom index:",sl
print(sl)
#opration on serises
print(sl+sl)
print(sl.max())

# accessing perticular element
print("Accessing element at 'a' key:",sl['a'])





