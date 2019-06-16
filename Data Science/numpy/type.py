import numpy

l=[1,5,15,5,51,15,51,5 ,'aadesh']
t=(11,11,23,14)
s={11,22,22,33,44,44,55,55}
d={'key1':1544,'key2':"Aadesh",'key3':"shraddha"}
arrl=numpy.array(l)
arrs=numpy.array(s)
arrt=numpy.array(t)
arrd=numpy.array(d)
print("1.List array:\n{}\n Sample array:\n{}\n Touple array:\n{}\n Directory array:\n{}".format(arrl,arrs,arrt,arrd))
# checkking types
print("Data Type of array list:",arrl.dtype)
print("Data Type of array touple:",arrt.dtype)
print("Data Type of array Sample:",arrs.dtype)
print("Data Type of array Dirctory:",arrd.dtype)


