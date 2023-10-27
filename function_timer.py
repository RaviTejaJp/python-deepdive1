import time

def time_it(function_name, *args, rep=1, **kwargs):
    start_time = time.perf_counter()
    for i in range(rep):
        function_name(*args, **kwargs)
    end_time = time.perf_counter()
    
    avg_runtime = (end_time - start_time)/rep
    print(f"Average runtime is {avg_runtime}")

time_it(print,1,2,3,4,5,sep="--",end="****\n",rep=6)
a = divmod(32,21)