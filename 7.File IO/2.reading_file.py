# reading file content as string

f = open('info.txt','r')
data = f.read()
print('File content is->',data)
f.close()