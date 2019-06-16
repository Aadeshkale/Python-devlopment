# accessing dictionary elements

l=[
    ('mango',100),
    ('apple',150),
    ('orange',100),
    ('grapes',220),
    ('berry',180),
    ('chiku',0)
]
d=dict(l)
print(d)
print()
print("Acessing element by key:",d['grapes'])

# by get method
print("Acessing element by get:",d.get('chiku'))

# when element is not present

print("Element is not preset:",d.get('aa'))
#key-error
print("Element is not preset:",d['aa'])



