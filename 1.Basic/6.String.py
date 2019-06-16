# Strings in python
s="Sachin"
s1="Mane"
print(s)
l = len(s) 
print("length of string is :",l)
print("Acessing single element:",s[0])
# Strings concatanation
con=s+s1
print(con)
print("length",len(con)) 
s+" Shivam"
print(s)   # polling concept i.e non mutable / immutable
# string spilt
sp=s.split('c') 
print(sp)
# string opration
print("Start to end:",s[0:])
print("Start to end:",s[1:4])
print("Start to end with dtep count 1:",s[1:4:1])# default step count 
print("Start to end with dtep count 2:",s[1:4:2])# step count = 2 
print("end to Start:",s[4:1])  # 4+1= 5 hence it is not reaching at end  
print("Start to end with dtep count -1:",s[1:4:-1])#  step count 
#reverse of String
rev=s[::-1]
print("reverse:",rev)
# String join
print("String join:","-".join(sp))
# string membership 
s in "S"
print("S" in s)
print("Sa" in sp)
print("z" not in s)
print("S" not in s)
# find 
print(s.find("Sa"))
print(s.find("xv"))
# index
print(s.index("Sa"))
print(s.index("xv"))