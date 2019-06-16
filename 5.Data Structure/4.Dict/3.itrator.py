# itrator on dictionary
d={
    'a':10,
    'b':24,
    'c':30,
    'd':12
}
print("My dicit:",d)
print()
# itrator
for i in d:
    print(i)
print()
for i in d:
    print(i,"->",d[i])
print()
for i in d:
    d[i]=d[i]*d[i]
    print(i,"->",d[i])
