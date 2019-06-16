# hirachical inheritance
class father():
    def __init__(self):
        print('This is father class properties')
class child1(father):
    def __init__(self):
        father.__init__(self)  # accessing father properties
class child2(father):
    def __init__(self):
        father.__init__(self)  # accessing father properties
c1=child1()
c2=child2()

print("--"*10)

# Multtiple inheritance
class x():
    a=10
    def __init__(self):
        print('This is x class')
class y():
    b=20
    def __init__(self):
        print('This is class y')

class op(x,y):
    def __init__(self):
        print('This is op class')
        s= x.a+y.b                # Acessing a form class x and b from class y
        print("Sum  is:",s)
        x.__init__(self)          # Acessing methods of class x class y
        y.__init__(self)
o=op()
print(o.b)  # acessing the parent properties through child class

print('--'*10)

# multilevel inheritance

class grangfather():
    def __init__(self):
        print('This is grand father properties')
class father(grangfather):
    def __init__(self):
        grangfather.__init__(self)
        print('This is father properties')
class boy(father):
    def __init__(self):
        print('This is child')
        father.__init__(self)
        grangfather.__init__(self)
b=boy()








