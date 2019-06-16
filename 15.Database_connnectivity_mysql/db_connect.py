import mysql.connector  # labrary for databse connection

con=mysql.connector.connect(host='localhost',database='sample',user='root',password='dx619') # method to connect database
buf=con.cursor()            # buffer between database and programm in ram


sql='select * from emp'     # sql query
buf.execute(sql)            # executing query
data=buf.fetchall()         # getting data form buffer  it return data in the form of list of tuple


for id,name,age,gender,salary,address in data:
    print('-'*60)
    print(id,"->",name,'->',gender,'->',age,'->',salary,'->',address)  # printing data
buf.close()