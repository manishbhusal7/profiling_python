

from simpleprofile import linear_search, binary_search
from functools import wraps
import random
import timeit
random.seed(0)

def create_list(k=100, max_val=None):
    max_val = k if max_val is None else max_val
    my_list = random.sample(range(0, max_val), k)
    my_list.sort()
    return my_list

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
    
    setup = '''
import random
random.seed(0)

k = 1_000
max_val = k * 3
my_list = create_list(k=k, max_val=max_val)
    '''

    timer = timeit.Timer('multi_run(linear_search, my_list, create_list(k=k))', setup=setup, globals=globals())
    results = timer.repeat(5, 30)
    avg = sum(results) / len(results)
    print(f"Linear Search Avg: {avg:.2} seconds")

    timer = timeit.Timer('multi_run(binary_search, my_list, create_list(k=k))', setup=setup, globals=globals())
    results = timer.repeat(30, 100)
    avg = sum(results) / len(results)
    print(f"Binary Search Avg: {avg:.2} seconds")

if __name__ == "__main__":
    main()



