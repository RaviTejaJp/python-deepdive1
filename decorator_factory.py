from functools import wraps
def timed(fn):
    @wraps(fn)
    def inner(*args,**kwargs):
        from time import perf_counter
        
        start = perf_counter()
        result = fn(*args,**kwargs)
        stop = perf_counter()
        
        print(f"Function {fn.__name__} ran with arguments{*args,*kwargs} in {stop-start} seconds")
        return result
    return inner



def fib(n: int) -> int:
    if n <2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
@timed
def calc_fib(n: int) -> int:
    return fib(n)



def dec_factory(a,b):
    print("Decorator factory has been called")
    def dec(fn):
        
        print(f"Decorator has been called")
        @wraps(fn)
        def executor(*args,**kwargs):
            print(f"Decorating factory function has variables {a,b}")
            print(f"Function {fn.__name__} called with {*args,*kwargs} arguments")
            return fn(*args,**kwargs)
        
        return executor
    return dec


def funtion_to_be_decorated(x,y):
    print(f"Actual function is called with {x,y} arguments")


funtion_to_be_decorated = dec_factory(1,2)(funtion_to_be_decorated)
funtion_to_be_decorated(10,20)

@dec_factory(100,200)
def funtion2_to_be_decorated(x,y):
    print(f"Actual function is called with {x,y} arguments")

funtion2_to_be_decorated(1000,2000)