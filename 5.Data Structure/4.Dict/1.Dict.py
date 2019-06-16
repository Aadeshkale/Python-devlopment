# creating dictionary ==> 'key':value

d={
    'aadesh':12,
    'sachin':13,
    'shubhangi':15,
    'gaurav':17
}
print("My 4.Dict\n",d)
#creating empty dictonary
d={}
print("Empty dictioary by {}:",d)
d=dict()
print("Empty dictioary by dict():",d)
# converrting other datastructure into dictionary

l=[['a',100]]
d=dict(l)
print(d)
print()

l=[('a',(10,12)),
   ('b',20),
   ('c',3),
   ('d',40)
]
d=dict(l)
print(d)
print()

t=(['mango',10],
    ['apple',20],
    ['grapes',40],
    ['orange',10]
)
d=dict(t)
print(d)
