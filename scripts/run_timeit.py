

from simpleprofile import linear_search, binary_search
from functools import wraps
import random
import timeit
import statistics
random.seed(0)

def create_list(k=100, max_val=None):
    max_val = k if max_val is None else max_val
    my_list = random.sample(range(0, max_val), k)
    my_list.sort()
    return my_list

def main():
    k = 10_000
    max_val = k * 3
    my_list = create_list(k=k, max_val=max_val)
    to_find = my_list[-1] # last element in the list

    timer = timeit.Timer('linear_search(my_list, to_find)', globals={**globals(), **locals()})
    results = timer.repeat(30, 1)
    avg = statistics.median(results)
    print(f"Linear Search Median: {avg*1000:.2f} ms")

    timer = timeit.Timer('binary_search(my_list, to_find)', globals={**globals(), **locals()})
    results = timer.repeat(30, 1)
    avg = statistics.median(results)
    print(f"Binary Search Median: {avg*1000:.2f} ms")

if __name__ == "__main__":
    main()



