import numpy as np
arr1=np.arange(1, 25)
arr1.resize(4,6)
arr2=arr1
print("arr1:\n",arr1)
print("arr2:\n",arr2)

# Arthameric oprations
print("Addition:\n",arr1+arr2)
print("Substraction:\n",arr1-arr2)
print("Multiplication:\n",arr1*arr2)
print("Division:\n",arr1/arr2)

# scalar opration
arr1**5
print(arr1,"\n")
arr1+100
print(arr1)


# univarsal opration
arr1.max()
arr1.min()
arr1.size
print("\n",np.sin(arr1))

# finding perticular no in array like even , odd  >3,<3
print("Graeather than 3\n",arr1[arr1>3])
print("Even:\n",arr1[arr1%2==0])


