# opration on dictionary
t=(
    ['key1',100],
    ['key2',120],
    ['key3',160],
    ['key4',150],
    ['key5',155]
)
d=dict(t)
print("My dict:\n",d)

# max-min by default work on first element
print("max:",max(d))
print("Min:",min(d))
# sorted- by default work on first element
print("sorted dict:\n",sorted(d,reverse=True))

# opration with coustom parameters
lt=d.items()
print(lt)
print()
# sorting
res=sorted(lt,key=lambda x:x[1])
print("res:",res)
for id,val in res:
    print(id,'->',val)
print()
#max-min
maximum=max(lt,key=lambda x:x[1])
print("maximum value:",maximum)


    