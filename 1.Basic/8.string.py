s='hello Aadesh'
print('1.',end='')
j=2
for i in s:
    print(i,end='')
    if i== ' ':
        print()    
        print('{}.'.format(j),end='')
        j+=1