# reduce function is used to reduce the result 

from functools import reduce
l=[2,7,5,4,12]
res=reduce(lambda x,y:x+y,l)
print(res)
