# enumarator on dictionary
d={
    'aadesh': [12,4000],
    'ravi':16,
    'shruti':18,
    'savita':19
}
print("My dict:\n",d)

for i,x in enumerate(d):
    print(i,'->',x,'->',d[x])
