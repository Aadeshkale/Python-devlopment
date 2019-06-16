# map function is used to apply specific functionality on each element of sequence 
l=[2,64,5,4]
def cube(x):
       return x**3
re=map(cube,l)
print(list(re))

# map with lambda
t=(2,5,3,6,4,5,5)
res=map(lambda x:x**3,t)
print(list(res))