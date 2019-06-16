from abc import ABC , abstractmethod   # recquried abc module ABC class for abstract class and method

class shape(ABC):
    @abstractmethod
    def display(self):              # this method should overidden by all childes of base class
        pass                        # abstract method should not have body, defination
    def fun(self):
        print('another method')


class circle(shape):
    def display(self):
        print('Drawing circle')
class rectangle(shape):
    def display(self):
        print('Drawing rectangle')
class trinagle(shape):
    def display(self):
        print('Drawing trinagle')

def canvs_draw(shape):
    for x in shape:
        x.display()


t=trinagle()
r=rectangle()
c=circle()
l=[t,r,c]

canvs_draw(l)

