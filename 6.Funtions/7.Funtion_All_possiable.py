# funtion with all possiable arguments
def fun(a,b,c=10,d=10,*args,**kwargs):
    print("All possiable args")


fun(10,122) # a= 10 , b=122 , c= 10 , d= 10 ,(),{}
fun(10,10,20,20) # a=10 , b=10 , c=10 , d=10 ,(),{}
fun(10,10,20,10,10,10,10,{'a',10}) # a=10 , b=10 , c=20 , d=10 ,(10,10,10),{'k' = 10 }
fun(10,20) # position args r ecrured