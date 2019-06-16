# single level inheritance

class animal():                    # base class

    def __init__(self):
        print('Animal is created')
    def eat(self):
        print('Animal is eating')

class dog(animal):                  # dirived class

    def __init__(self):
        animal.__init__(self)       # accessing animal class properties
        print("Dog is Created")
        animal.eat(self)
d=dog()
