# local() and global() variabels
g=10

def fun1():
    # checking scope of variable
    g= 8.3
    print(locals())
    print(globals())
    print(g)

fun1()

print()

def fun2 ():
    global g
    g=20
    print(g)
fun2()





