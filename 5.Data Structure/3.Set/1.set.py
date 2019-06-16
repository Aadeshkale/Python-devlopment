# sets are mutable , store hashable iteams
s={121,12,12,12,12,"a","a","a",3,5,6}
print(s)
# defineing empty sets
s={} # treated as dictionary
print(type(s))
s=set()
print(type(s))
print()
# converting list to set
l=[12,12,12,12,12,13,13,13,14,15,16,17]
s=set(l)
print(s)
