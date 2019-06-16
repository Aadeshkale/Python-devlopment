# used for data Abstraction
# private member created with the the help of '__' oprator
class emp():

    __x=10      # private member  indicated by '__'
    __y=20      # private member

    def __fun(self):
        print('This is private method')

    def _fun2(self):         # coding standard '_' for testing purpose
        print('This funtion is created for testing purpose programmer can use at own risk')

    def __init__(self,name,id): # special method called automatically when objects of class is created
        self.name=name
        self.id=id

e=emp('sachin',123)

e.fun()            # error we can't access private members outside of class
print(e.x)         # error we can't access private members outside of class

