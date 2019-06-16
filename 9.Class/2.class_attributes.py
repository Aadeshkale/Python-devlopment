class vehicle():

    work='travling'                    # class static attribute same for all instance

    def __init__(self,type,name):  # special method called automatically when objects of class get initilized
        self.name=name             # self keyword is indicate that self class type
        self.type=type


v1=vehicle(type='car',name='tata')   # creating and initilation of objects of class
v2=vehicle(type='bike',name='honda')

print(v1.type,"->",v1.name)           # accessing properties of objects
print(v2.type,"->",v2.name)
print(v1.work)

