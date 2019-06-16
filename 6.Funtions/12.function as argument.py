# passing function as argument to another function


def add(x,y):
    print(x+y)
def volume(a,b,c):
    print(a+b+c)

def cal(f,*args,**kwargs):
    f(*args)

cal(add,25,32)
cal(volume,12,13,14)