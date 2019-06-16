f=open('input.txt','r')
s=f.readline()
length=len(s)
print(s)
res=''
for i in range(0,length):
    if(s[i]=='1'):
        res+='one'+' '
    if (s[i] == '2'):
        res += 'two' + ' '
    if (s[i] == '3'):
        res += 'three' + ' '
    if (s[i] == '4'):
        res += 'four' + ' '
    if (s[i] == '5'):
        res += 'five' + ' '
    if (s[i] == '6'):
        res += 'six' + ' '
    if (s[i] == '7'):
        res += 'seven' + ' '
    if (s[i] == '8'):
        res += 'eight' + ' '
    if (s[i] == '0'):
        res += 'zero' + ' '
f.close()
f=open('output.txt','w')
f.write(res)