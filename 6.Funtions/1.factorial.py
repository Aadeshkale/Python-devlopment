# factorial programm of gien no
n=int(input("Enter ur no:"))

fact=1

for i in range(1,n+1):
    fact=i*fact
print("Factorial of {} is :{}".format(n,fact))
