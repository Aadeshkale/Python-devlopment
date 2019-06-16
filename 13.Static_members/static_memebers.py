class students():
    year='Final Fear' # common for all objects Static member can access through Class Name and '.'

    def __init__(self,name='nan',id='nan',address='nan'):
        self.id=id
        self.name=name
        self.address=address

    @staticmethod
    def fun():
        print('This is an Static method')

    def __str__(self):
        return  students.year+"->"+self.name +"->"+ self.id +"->"+ self.address


s1=students()
s2=students('Sachin','12','N2 cidco')
print(s1)
print(s2)
students.fun()  # Accessing static method with class name and '.'


