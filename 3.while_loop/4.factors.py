# find factors of given no's
n=int(input("Enter ur no:"))
i=1
while i<=n:
	if n%i==0:
		print(i)
	i+=1
print("The End")