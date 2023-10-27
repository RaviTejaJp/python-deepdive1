def timed(fn):
    from functools import wraps
    from time import perf_counter
    
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        stop = perf_counter()
        elapsed = stop - start
                
        args_ = [str(item) for item in args]
        kwargs_ = [ f"[k]=[v]" for (k,v) in kwargs.items()]
        all_params = ' '.join(args_+kwargs_)
        print(f"{fn.__name__} with args {all_params} took {elapsed:6f} seconds")

        return result
    return inner

def fib_rec(n : int) -> int:
    """_summary_

    Args:
        n (int): _description_

    Returns:
        _type_: _description_
    """
    if n <=2:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

def fib_rec_caching(n: int, cache: dict = {}) -> int:
    """_summary_

    Args:
        n (int): _description_
        cache (dict): _description_

    Returns:
        int: _description_
    """
    if n in cache:
        pass
    elif n <= 2:
        cache[n] = 1
    else:
        cache[n] = fib_rec_caching(n-1) + fib_rec_caching(n-2)
    return cache[n]


def fib_loop(n: int)-> int:
    fib_1 = 1
    fib_2 = 1
    
    for i in range(3,n+1):
        fib_1, fib_2 = fib_2, fib_1+fib_2
    return fib_2

@timed
def func_caller(func_name, *args,**kwargs):
    return func_name(*args,**kwargs)


def fib_reduce(num: int) -> int:
    from functools import reduce
    initial = (0,1)
    dummy = range(num)
    fib_n = reduce(lambda prev, num : (prev[0]+prev[1], prev[0]),dummy, initial)
    return fib_n[0]  

@timed
def main():
    func_caller(fib_reduce, 2000)

if __name__ == '__main__':
    main()