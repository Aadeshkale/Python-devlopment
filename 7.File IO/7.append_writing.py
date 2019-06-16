# append writing
f=open('info.txt','a')
f.write('\nAdding data at the end of file')
f.close()

# reading file content
f=open('info.txt','r')
data=f.read()
print(data)


