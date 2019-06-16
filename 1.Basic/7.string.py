s='12 hello 456 hi12'
for i in s:
    if i in "0123456789" or i==" ":
        print(i,end='')
