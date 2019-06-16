# diamond problem caused by multiple inhetitane
class z():
    a=10
    def zmethod(self):
        print('this is class z method')

class x(z):
    a=20
    def zmethod(self):
        print('this is class x method')

class y(z):
    a=30
    def zmethod(self):
        print('this is class y method')
class op(x,y):
    def opmethod(self):
        print('This is class op method')
        print("value of a:",x.a)

o=op()
o.opmethod()
o.zmethod()                     # which method is called is defined by the sequence of inheritance i.e. FCFS

# if we want to change behaviour at run time the we have to use __bases__ attribute

o.__bases__=(y,x)
o.zmethod()







