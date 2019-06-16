# finding count of each no in list

l=[12,12,12,2,2,5,5,5,3,5,2,2,]
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)