s={'Apple','Orange','khiku'}
print(s)
print()
# adding new elements to set
s.add('Apple')
s.add("Grapes")
print(s)
print()
# removeing elements form set
s.remove('Apple')
# s.remove('aade') -> element is not present it throws KeyError
print(s)
s.discard('aade') # similar to remove but dosen't fetch error when element is not present
# pop opration
s.pop()
s.pop()
s.pop()
print(s)
