from functools import wraps, partial
import logging


def custom_logger(function):
    logging.basicConfig(level=logging.INFO,filename="closures.log")
    
    @wraps(function)
    def date_logger(*args,**kwargs):
        logging.info(f"Running {function.__name__}")
        return function(*args,**kwargs)
    return date_logger

@custom_logger
def add(x,y):
    return x + y

@custom_logger
def sub(x,y):
    return x - y

for i in range(0,10):
    print(add(i,i+1))
    print(sub(i-1,i+1))

    