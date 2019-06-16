# genetartor is am python itrator object which yeild values as they process
# unlike return it will return all values after the processing
# it does not return single value untill hole function processing is done. 

def fun(l):
    for i in l:
        yield(i*i)   

f = fun([12,25,56,23])
print(f)
print(next(f))   # before processing next element it returns privious element by kepping funtion state as it is.
print(next(f))
print(next(f))
print(next(f))
