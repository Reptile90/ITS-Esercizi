'''Write a Python function that takes a list and returns a new list with distinct elements from the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]'''


def list_creator(number_list:list[int])->int:
    unique_list:list[int] = []
    for numero in number_list:
        if numero not in unique_list:
            unique_list.append(numero)
    print(f" Sample List: {number_list}")
    return unique_list


print(f" Unique List : {list_creator([1,2,3,3,3,3,4,5])}")


