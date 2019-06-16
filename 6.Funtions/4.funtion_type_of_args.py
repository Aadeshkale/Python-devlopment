# positional arguments -> mandotary arguments
def fun(x,y,z):
    res=max(x,y,z)
    return res
maximum=fun(15,85,5) # positional arguments
print("maximum value:",maximum)
print()

# key arguments -> passing args with key
maximum=fun(z=100,x=20,y=30)
print("maximum:",maximum)
# maximum(z=10,20,30) # keyargument must follow position argument
# res=fun(1,25,y=10)  # multiple value for 'y'
print()

# default argunents

def add(c,a=0,b=0): # default args must follow positional args
    s=a+b+c
    return s
print("addition is:",add(30))

# add(a=0,b=0,c=10) # not allowed
# actual args replaces default args
print("Addition is :",add(20,30,40))
