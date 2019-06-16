f=open('info.txt','w')
f.write('''
    so ,please open ur laptop and start with pycharm,
    first You have to create your file then,
    you can perform read-write opration  
''')
f.close()
# reading file content

f=open('info.txt','r')
data=f.read()
print('File-content is->',data)