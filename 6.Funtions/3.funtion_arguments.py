
#function with no arg & return
def wel():
    print("welcome")
wel()
# funtion with three args & no return funtion
def fun(x,y,z):
    print("x:",x)
    print("y:",y)
    print("z:",z)
fun(10,20,30)

# funtion with multiple return value
def avg(x,y):
    total=x+y
    res=(x+y)/2
    return total,res
# unpacking  we can not access variabels of the funtion outside of the body directly
total,res=avg(15,11)
print("Sum is:{} avarage is:{}".format(total,res))
print()
# funtion argument passing
def add(x,y):  # formal parameters
    z=x+y
    return z
a=10
b=35
print("addition is:",add(a,b)) # actual argument
print()




