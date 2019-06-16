class book():

    def __init__(self,name,title,pages):
        self.name=name
        self.title=title
        self.pages=pages

    def __str__(self):              # special function to decide what return at onject string representation
        return 'name:{} title:{} pages {}'.format(self.name,self.title,self.pages)

    def __len__(self): # special function to decide what return at len function
        return self.pages

b=book('python','begining of python',200)
print(b)
print(len(b)) 