from typing import List
from bisect import bisect_left

def linear_search(my_list:List, value:int) -> int:
    for i, item in enumerate(my_list):
        if item == value:
            return i
    return -1

def binary_search(my_list:List, value:int) -> int:
    hi = len(my_list)
    pos = bisect_left(my_list, value) # find insertion index
    if pos != hi and my_list[pos] == value:
        return pos
    else:
        return -1
