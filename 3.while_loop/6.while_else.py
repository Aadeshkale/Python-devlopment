# while-else example
n=int(input("Enter ur no:"))
i=2
while i<n:
	if n%i==0:
		print("no is not prime")
		break
	i+=1
else:
	print("no is prime")