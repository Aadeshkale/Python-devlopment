# writing information into file

f=open('info.txt','w')
f.write('The new information is added.\nToday we learn about python file input output oprations.\n so be ready.')
f.close()

f=open('info.txt','r')
data=f.read()
print('File Content:->',data)
f.close()


