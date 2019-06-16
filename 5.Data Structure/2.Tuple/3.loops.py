#while
t=(12,11,12,12,'aade','s')
print("len:",len(t))
i=0
while i<len(t):
    print(t[i])
    i+=1
print("end of loop")

# for
for i in t:
    print(i)
print("end of for loop")

# range attributes are compalsury
for v in range(0,6):
    print(t[v])
    
