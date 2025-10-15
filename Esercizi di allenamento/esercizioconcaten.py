def filter_and_concat(nums:list[int], min_val:int):
    stringa=""
    for num in nums:
        if num > min_val:
            stringa += str(num) + ","
    if stringa.endswith(","):
        stringa = stringa[:-1]
    return stringa


lista = [1,3,2,5,4,5,6,5,4,3]
min = 3
print(filter_and_concat(lista,min))