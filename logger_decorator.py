

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


def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone
    
    @wraps(fn)
    def inner(*args,**kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args,**kwargs)
        print(f"{run_dt}: called {fn.__name__}")
        import time
        time.sleep(3)
        return result
    return inner



@timed
@logged
def add(x,y):
    return x + y

@timed
@logged
def sub(x,y):
    return x - y
@logged
def main():
    print(add(1,2))
    print(sub(1,3))

if __name__ == "__main__":
    main()
        