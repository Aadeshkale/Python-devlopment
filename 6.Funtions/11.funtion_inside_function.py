# funtion passing to another function

def fun():
    print('this is passed function')
print(fun())   # by default it retrns none

def greet():
    print('this is greet function')

def ok(f):
    f()  # here greet becomes function
ok(greet)

print()

# function inside function

def cal(n):
    pi=3.14
    def area():
        r=n
        a=r*r*pi
        return a
    area()
    return area()  # function return function
print(cal(5))


