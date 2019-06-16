# function variable key words args

def add(**kwargs):
    s=0
    print(type(kwargs))
    lt=kwargs.items()
    for i,x in lt:
        s=s+x
    print(s)
add(a=10,b=20,c=30)