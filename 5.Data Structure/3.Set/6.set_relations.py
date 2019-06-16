s={4,5,6,7,7,8,9}
s1={4,5,4,1,2,3}
print(s)
print(s1)
print()
# union i.e '&'
s3=s1.union(s)
uni=s1&s
print("union:",s3)
print("union by using '&' :",s3)

# intersection i.e '|'
s3=s.intersection(s1)
common=s|s1
print("intersection:",s3)
print("intersection using '|':",common)

# diffrence
diff=s.difference(s1)
print("diffrence:",diff)
diff=s-s1
print("diffrence using '-':",diff)
