class car():
    __model=2018
    def __fun(self):
        print('This is private member of class')

    def __init__(self,color='white'):
        self.color=color
c=car()
print(car.__dict__) # Acessing object in the form of dict
print(car._car__model)