# squaring each element
l=[15,55,56,45,65]
# here i is an temprary variable
for i in l:
    i=i*i
print(l)
# actual squaring
for i in range(0,len(l)):
    l[i]=l[i]*l[i]
print(l)
