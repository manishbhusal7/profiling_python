from simpleprofile import linear_search, binary_search
from functools import wraps
import random
import time
random.seed(0)

def create_list(k=100, max_val=None):
    max_val = k if max_val is None else max_val
    my_list = random.sample(range(0, max_val), k)
    my_list.sort()
    return my_list

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = (end_time - start_time) * 1000
        print(f'Function {args[0].__name__} Took {total_time:.1f} ms')
        return result
    return timeit_wrapper

def multi_run(fn, my_list, values_to_search):
    results = []
    for value in values_to_search:
        idx = fn(my_list, value)
        results.append(idx)
    return results

def main():
    k = 1_000
    max_val = k * 3

    my_list = create_list(k=k, max_val=max_val)

    # Example query
    value = 7 # 7
    idx  = linear_search(my_list, value)
    print(f"Index of {value} is {idx}")

    
    multi_run(linear_search, my_list, create_list(k=k))




if __name__ == "__main__":
    main()