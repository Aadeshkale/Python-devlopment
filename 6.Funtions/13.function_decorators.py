# decorator -> design pattern -> to add new funtionality to existing function without modifing it

def add(x,y):
    print(x+y)
    return x+y

def decorate(f,*args):             #decorator
    print('*********************')
    f(*args)
    print('*********************')

decorate(add,20,30)               #calling function with decorator


# decoder ->






