for i in range(1, 6):
    for j in range(1,i):
        print(j,end="")
    print()

print("Simply in reverse order")
for i in range(1,6):
     for j in range(i,0,-1):
       print(j,end="")
     print()

print("priting number in reverse order")
for i in range(6,0,-1):
    for j in range(1,i):
        print(j,end="")
    print()

print("priting stars")
for i in range(1,6):
     for j in range(1,i):
       print('*',end="")
     print()

print("priting stars in reverse order")
for i in range(6,0,-1):
    for j in range(1,i):
        print('*',end="")
    print()
    
for i in range(1,6):
    for j in range(6,i,-1):
        print(' ',end="")
    for k in range(1,i):
        print('#','',end="")
    print()

for num in range(1,6):
    print(num)