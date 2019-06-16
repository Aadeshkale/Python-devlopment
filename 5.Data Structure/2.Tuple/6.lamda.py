# lamda function :- one line function

f=lambda x,y:x+y
print("Addition funtion:",f(5,6))

f=lambda x:x*x
print("Square funtion:",f(5))

f=lambda x,y:x*y
print("Multiplication funtion:",f(5,9))
print()
# passing data structor to lambda

l=[12,121,121,124]
t=121,21,21,194
s="Apple"
key=lambda x:x[3]
print("list parameter :",key(l))
print("tuple parameter:",key(t))
print("string parameter:",key(s))
