# reading file content line -by line by for

f=open('info.txt','r')
for line in f:
    print(line)
f.close()