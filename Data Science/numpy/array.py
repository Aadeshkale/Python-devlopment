import numpy # importing numpy labrary

# converting any tye into array

l=[12, 45, 454, 8787, 89, 56, 56,"aa"]
t=(12, 13 , 14 ,5 ,6)
s={1, 2, 3, 4, 5}
d={'key1':12, 'kay2':14}
arrl=numpy.array(l)
arrt=numpy.array(t)
arrs=numpy.array(s)
arrd=numpy.array(d)
print("Array of list:", arrl)
print("Array of touple:", arrt)
print("Array of sets:", arrs)
print("array of dictionary:", arrd)

# array with range

arr=numpy.arange(0,25)
print(arr)

# reshape
arr.reshape(5,5)
print(arr)

# array with random no

arr=numpy.random.rand(5)
print("random no with normal distrubtion", arr)
print()
arr=numpy.random.rand(5,5)
print("random no with normal distrubtion", arr)
print()
arr=numpy.random.randn(5)
print("random no with standred distrubtion", arr)
print()
arr=numpy.random.randint(1,5,10)
print(arr)

# array indexing
arr=numpy.arange(1,11)
print("arr:", arr)
print(arr[2])

# two diamentional array
l=[[54,45,2,4],[1,88,4,5],[12,36,65,5,]]
arr=numpy.array(l)
print("two diamensional array:", arr)
print()
# array slicing
a=numpy.arange(1,25)
a.resize(3, 6)
print(a)
print()
print(a[0:2,5:6])
