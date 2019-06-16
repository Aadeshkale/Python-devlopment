import io
# sovle porinter problem for reading content form file

f=open('info.txt','w+')
f.write('Solving \ncursor \nproblem for \nreading \ninformation ')

# problem due to cursor position
data=f.read()
print(data)

# tells current position of cursor
position=f.tell()
print("Current position after write opration:",position)
print()



# use of seek
f.seek(0,io.SEEK_SET)   # seting pointer location to a pertiular location
data=f.read()
print(data)             # after reading data cursor position is again set to end of file
f.seek(0,io.SEEK_SET)
print(f.tell())

f.close()
