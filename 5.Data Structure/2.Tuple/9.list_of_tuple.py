l=[('apple',20),('pineapple',30),('mango',40),('chiku',20),('grapes',30)]
print(l)
print()
# itrator
for i in l:
    print(i)
print()
# acceing each element with index
for i in l:
    print(i[0],'->',i[1])
print()
# unpacking
print()
for fruit,count in l:
    print(fruit,"-->",count)
print()
# finding elements haveing more count than 30
for fruit,count in l:
    if count>30:
        print(fruit,"-->",count)
print()

# unpacking for clean code for list of tupel
emp_db=[(12,'sachin','math',40000),
        (18,'kunal','english',50000),
        (13,'sshraddha','account',40000),
        (14,'shivam','comp',30000),
        (18,'shyam','math',36000),
        (16,'shuchita','math',36000)

]
for id,name,*_ in emp_db:
    print(id,'-->',name)
# Print all the employees whose salaries are greater than the average salary.
total_sal=0
for *_,sal in emp_db:
    total_sal+=sal
print("total Salary:",total_sal)
length=len(emp_db)
print("total no of employee:",length)
avg=total_sal/length
print("Avarage salary:",avg)
print("emplyee with avg salary:")
for id,name,*_, sal in emp_db:
    if sal<=avg:
        print(id,'==>',name)
print()
# if we print multipple perticular values it will return a list
for *other,sal in emp_db:
    print(sal,"-->",other,type(other))


