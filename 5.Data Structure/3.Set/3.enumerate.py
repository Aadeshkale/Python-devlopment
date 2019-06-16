s={12,12,12,2,5,54,4,6,6}
print(s)
for i,x in enumerate(s):
    print(i,":",x)
print()
for i,x in enumerate(s,start=1):
    print(i,"->",x)