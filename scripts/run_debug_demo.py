from simpleprofile import linear_search, binary_search, custom_binary_search, insert
from typing import List


 #  There is a bug in here
def add_num(my_list: List[int]):
    value = input("Add a number: ")
    insert(my_list, value)

# some bugs in here
def search_num(my_list: List[int]):
    command = input("Choose a search method: linear, binary, custom: ")
    value = input("Choose a number to search for: ")
    if command == "lnear":
        index = linear_search(my_list, value)
    elif command == "binary":
        index = binary_search(my_list, value)
    else:
        index = custom_binary_search(my_list, value)
    
    print(f"The number {value} is at index {index}")

def main():

    my_list = [1, 4, 7, 8, 10]
    while(True):
        print(f"Current list: {my_list}")
        command:str = input("Choose an operation, add or search: ")
        if command == "add":
            add_num(my_list)
        elif command == "search":
            search_num(my_list)
        print()



if __name__ == "__main__":
    main()