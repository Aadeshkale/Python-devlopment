# print prime no's in perticular range
s=int(input('Enter ur start no:'))
n=int(input('Enter End no :'))

for i in range(s,n+1):
    sr = int(i ** 0.5)
    for j in range(2,sr+1):
        if(i%j==0):
            break
    else:
        print(i)



