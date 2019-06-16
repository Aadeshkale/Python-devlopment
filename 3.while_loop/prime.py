# programm for to check no is  prime number
n=int(input("Enter no:"))
i=2	
while i<n:
	if n%i==0:
		 flag=0
		 break
	else :
		flag=1
	i+=1
if flag==0:
	print("no is not prime")
else:
	print("no is prime")

	