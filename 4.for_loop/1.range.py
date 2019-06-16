# range Example
r = range(5)
print(r)
# range returns list type
l=list(range(5))

print(l)

# range with itrator

for x in  range(1,11):
 	print(x,end='')
print()
# even no's

for  num in range(2,22):
	if num%2==0:
			print(num)	
# range with step count odd
for num in range(1,21,2):
	print(num)
# range with step count even
for num in range(2,22,2):
	print(num)
print()	
# in reverse order	
for num in range(10,0,-1):
	print(num)
