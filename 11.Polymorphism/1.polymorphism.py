# add new changes into existing object oriented system without modifing it .
# creating single interface for multiple funtionalities .
# it follows IS-A reletionship , cosider following example

class animal():
    def walk(self):
        print('animal is walking')

class hourse(animal):
    def walk(self):
        print('hourse is walk on four legs')

class man(animal):
    def walk(self):
        print('man walk on two legs')

h=hourse()
h.walk()
m=man()
m.walk()
    