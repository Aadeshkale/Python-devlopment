# programm to check given tiangle is Right angle Triangle

a=int(input('enter a:'))
b=int(input('enter b:'))
c=int(input('enter c:'))

if a+b>c or a+c>b or c+b>a:
    print('it is an valid triangle')
    if (a**2)+(b**2)==(c**2) or (a**2)+(c**2)==(b**2) or (b**2)+(c**2)==(a**2) :
        print('it is an right angle triangle')
    else:
        print('it is not an right angle triangle')
else:
    print('it is not an valid triangle')
