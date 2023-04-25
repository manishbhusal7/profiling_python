from simpleprofile import linear_search, binary_search
import random
import time
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
    to_search = create_list(k=k, max_val=max_val)

    while(True):
        choice = random.randint(0, 1)
        if choice == 0:
            print("Run Linear")
            multi_run(linear_search, my_list, to_search)
        else:
            print("Run Binary")
            multi_run(binary_search, my_list, to_search)
        
# sudo py-spy record -o profile.svg -- python scripts/run_pyspy_demo.py
if __name__ == "__main__":
    main()