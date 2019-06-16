# reading file content in for of lines i.e list of line

f=open('info.txt','r')
data=f.readlines()    # return list of lines>strings
print(data)
f.close()

