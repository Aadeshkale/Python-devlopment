# enumarator funtion return an secquence no,actual element
l=["apple",'orange','mango','pineapple','graps']
print(l)
for i,fruit in enumerate(l):
    print(i,":",fruit)

#enumarate with coustom start index it accept only int
print()
for i,item in enumerate(l,start=1):
    print(i,":",item)
print()
# square with enumarate

l2=[2,3,4,5,6]
print(l2)
for i,x in enumerate(l2):
    l2[i]=x*x
print(l2)
