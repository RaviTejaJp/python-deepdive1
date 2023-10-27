from typing import Any
from time import perf_counter,sleep
from functools import wraps

class TimeItDecorator:
    def __init__(self,reps) -> None:
        self.reps = reps
    
    def __call__(self,func) -> Any:
        @wraps(func)
        def wrapper(*args, **kwds):
            time_taken = 0
            for item in range(self.reps):
                start_time = perf_counter()
                result = func(*args, **kwds)
                end_time = perf_counter()
                # sleep(1)
                time_taken += end_time - start_time

            print(f"{func.__name__} with parameters {args,kwds} took {time_taken/self.reps} seconds")
            return result
        return wrapper

@TimeItDecorator(reps=10)
def sub(a: int, b:int)-> int:
    return a - b

def add(a: int, b:int)-> int:
    return a + b

TimeItDecorator(reps=10)(add)(10,20)
sub(20,10)

class TimeItDecoratorWithoutParam:
    def __init__(self,func) -> None:
        self.func = func
    
    def __call__(self,*args,**kwds) -> Any:
        start_time = perf_counter()
        result = self.func(*args, **kwds)
        end_time = perf_counter()
        time_taken = end_time - start_time
        print(f"{self.func.__name__} with parameters {args,kwds} took {time_taken} seconds")
        return result

@TimeItDecoratorWithoutParam
def mul(a: int,b: int)-> int:
    return a*b

def div(a:int, b:int)-> int:
    return a/b if b!=0 else "DivisionByZero"

TimeItDecoratorWithoutParam(div)(10,2)
mul(10,20)