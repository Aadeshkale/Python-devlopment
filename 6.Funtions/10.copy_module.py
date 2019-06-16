# copy module in python
import copy
def fun(p):
    p[1]=100 # here both p and l refers same list so it modify it's contain

def main():
    l=[12,2,31,31]
    print("Original list:",l)
    fun(l)
    print("Modified list:",l)
main()

# prevent this situation using copy-> shallow copy

def main():
    l=['a','b','c']
    print("Original list:",l)
    dup=copy.copy(l)
    fun(dup)
    print('original list conent',l)
    print("Modified list",dup)
main()
print()
print('Sallow copy problem')
# shallow copy problem
def fun(p):
    p[1][0]=3


def main():
    l=[12,[2,2],4]
    print('Original list:',l)
    dup=copy.copy(l)
    fun(dup)
    print('Original list cntent:', l)
    print('Duplicate copy:',dup)
main()
print()
print('sallow copy problem resolved by deepcopy')
# shallow copoy problem resolved by deepcopy
def fun(p):
    p[1][1]=100

def main():
    l=[12,[4,5,6],23]
    print("original list",l)
    dup=copy.deepcopy(l)
    fun(dup)
    print("original list content",l)
    print("modified list",dup)
main()