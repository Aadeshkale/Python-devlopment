# function variable args -> take arguments in the form of tuple

def add(*args):
    s=0;
    print(type(args))
    for i in args:
        s=s+i
    print(s)

add(1,1,1,2,3,1,1)
