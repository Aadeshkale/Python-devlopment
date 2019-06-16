# programm for calculating income tax on salary
salary=int(input("Enter the salary:"))
Actual_salary=salary
ttax=0
if salary>1000000:
	slab = salary-1000000
	tax = slab*30/100
	ttax += tax
	salary -= slab

if salary>500000:
	slab = salary-500000
	tax = slab*20/100
	ttax += tax
	salary -= slab

if salary>300000:
	slab=salary-300000
	tax = slab*10/100
	ttax += tax
	salary -= slab

if salary<300000:
	print("No tax!!")
	
print("salary={} Tax={} ".format(Actual_salary,ttax))	