# filter function is used to filter elements form sequence 
l=[2,6,5,3,4]
def fun(x):
    if x%2==0:
       return x
res=filter(fun,l)
print(list(res))

# filter with lambda
l=[12,2,5,7,3,2,5,66]
res=list(filter(lambda x:x%2==0,l))
print(res)
