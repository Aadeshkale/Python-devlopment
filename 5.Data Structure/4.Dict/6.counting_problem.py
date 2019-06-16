l=[1,1,1,2,2,6,5,6,5,5,3,2,4,3]
print(l)
# traditional way
for i in l:
    print(i,"->",l.count(i))

# with dictionary
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)