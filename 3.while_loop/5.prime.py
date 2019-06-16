# prime no with squreroot therom
n=int(input("Enter ur no:"))
i=2	
sr=n**0.5 # i.e no ^ 1/2
while i<=sr:
	if n%i==0:
		flag=0
		break
	else:
		flag=1
	i+=1
if flag==0:
	print("no is not prime")
else:
	print("no is prime")