# Optional Parameters

def func(x):
    return x**2

call = func(5)
print(call)

def func(x = 1): # x = 1 defauly or optional parameter
    return x**2

call = func(3)
print(call)

call = func() # gives no error without an argument
print(call)

def func2(name, freq = 1):
    print(name*freq)
call = func2('tim ', 3)
func2('tim ')
func2(5)

def func2(name, add =5, freq = 1):
    print(name*(freq+add))

call = func2('tim ', 3)
func2('tim ')
func2(5)
func2(5,0,1)