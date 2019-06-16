l=['shivam',121,'kunnal','pranita','sachin',123.36]
# length of list

length=len(l)
print("length of list:",length)

# list indexing

print("iteam:",l[0])
print("last iteam of list:",l[length-1])
print(l[len(l)-1])

# modifing value at an index

l[0]='sonu'
print("Modifing value at l[0] location:",l)

# adding element

l.append("rach") # to add at last of list
print("append at last location ",l)

l.insert(6,"rachana") # insert element at perticilar location
print("adding iteam at l[6] location:",l)

# removeing element

l.pop() # removeing last element
print("Removed by pop():",l)
l.pop(3) #
print("remove element at l[3] location ",l)
l.remove('sonu') # removing perticular element by value
print(" removing item by remove():",l)
print()
#reverse of list
l.reverse()
print(l)

