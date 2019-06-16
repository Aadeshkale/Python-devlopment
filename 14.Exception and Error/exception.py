# simple python exception demo

try:                          # code cause error should be in try block
    a=10
    b=0
    print(a//b)
except Exception as err:    # except is used to handle error
    print('Exception has occured',err)  # Exception class is super class for all error handling
    # error
else:
    print('working')        # if there is no exception in try block then it is executed
finally:   # executed cumpalsary as well as used to handle error occured in exception block
    print('Programm exection is continous')
