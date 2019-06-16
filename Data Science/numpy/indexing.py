import numpy
arr=numpy.arange(0,24)
arr.resize(4,6)
print(arr)

print("Acessing single element:\n",arr[2][4])
row=arr[0:1]
print("Acessing single row:",row)

# by using slicing
print("Acessing two rows:\n", arr[1:3])
print("Accessing two cols:\n",arr[0:,3:5])
print("Acessing perticular elements:\n",arr[2:4,3:5])

