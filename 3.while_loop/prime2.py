# prime no with reduced itration
n=int (input("Enter Ur no:"))
i=2
while i<n//2:
	if n%i==0:
		flag=0
	else:
		flag=1
	i=i+1	
if flag==0:
	print("no is not prime")
else:
	print("no is prime")