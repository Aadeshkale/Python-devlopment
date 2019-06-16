emp_db=[
    (12,'sachin','math',24),
    (13,'shivam','math',23),
    (14,'shraddha','history',24),
    (15,'kunal','science',20),
    (16,'shyam','sanskurt',19)
]
for id,nsme,sub,age in emp_db :
    print(id,"-",nsme,"-",sub,"-",age)
print()
soterd_db = sorted(emp_db)

for id,nsme,sub,age in soterd_db :
    print(id,"-",nsme,"-",sub,"-",age)
print()
print("Sorting with perticular property like age:")
# sorted funtion function accepts data-structure,key parameter
soterd_db=sorted(emp_db,key=lambda x:x[3])

for id,nsme,sub,age in soterd_db :
    print(id,"-",nsme,"-",sub,"-",age)





