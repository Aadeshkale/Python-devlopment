l=[0,1,0,1,1,0,1]
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l)
