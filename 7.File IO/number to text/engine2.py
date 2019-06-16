# simply num to string
f=open('input.txt','r')
f2=open('output.txt','w')
for line in f:
    res = ''
    for i in range(0,len(line)):
        if (line[i] == '1'):
            res += 'one' + ' '
        if (line[i] == '2'):
            res += 'two' + ' '
        if (line[i] == '3'):
            res += 'three' + ' '
        if (line[i] == '4'):
            res += 'four' + ' '
        if (line[i] == '5'):
            res += 'five' + ' '
        if (line[i] == '6'):
            res += 'six' + ' '
        if (line[i] == '7'):
            res += 'seven' + ' '
        if (line[i] == '8'):
            res += 'eight' + ' '
        if (line[i] == '9'):
            res += 'nine' + ' '
        if (line[i] == '0'):
            res += 'zero' + ' '

    f2.write(res+'\n')

