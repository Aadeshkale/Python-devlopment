# finding biggest no in a list
l=[12,5,66,11,65,15,66.232,45] # list should be homogenous
print("Biggest no:",max(l)) # max() for finding biggest no in list

# finding biggest no with for loop
bigno=l[0]
for i in range(0,len(l)):
    if bigno<l[i]:
        bigno=l[i]
print("big no is:",bigno)
