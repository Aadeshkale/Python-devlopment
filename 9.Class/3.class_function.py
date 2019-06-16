class circle():
    pi=3.14
    def __init__(self,radious):
        self.radious=int(input('Enter ur radious:'))

    def area(self):
        return self.radious**2*circle.pi

c1=circle(1)         # we have to pass positional arguments
print(c1.area())