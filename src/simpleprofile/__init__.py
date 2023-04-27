from typing import List
from bisect import bisect_left, insort



def linear_search(my_list:List, value:int) -> int:
    for i, item in enumerate(my_list):
        if item == value:
            return i
    return -1

def binary_search(my_list:List[int], value:int) -> int:
    hi = len(my_list)
    pos = bisect_left(my_list, value) # find insertion index
    if pos != hi and my_list[pos] == value:
        return pos
    else:
        return -1


def insert(my_list:List[int], value:int):
    insort(my_list, value)
    return my_list
    
# There are a few bugs here! Lets see if we can find them
def custom_binary_search(my_list:List[int], value:int) -> int:
    """Will perform a binary search in the provided list

    Args:
        my_list (List[int]): A list of integers
        value (int): A value to find in the list

    Returns:
        int: The index of the value in my_list. If not found return -1
    """
    hi = len(my_list) - 1
    lo = 0
    while (lo <= hi):
        mid = (hi + lo) / 2
        if my_list[mid] == value:
            return mid
        elif value < my_list[mid]:
            hi = mid - 1
        else:
            lo = mid
    return -1


