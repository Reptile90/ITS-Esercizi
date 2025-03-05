'''Write a function check_each(), which takes a list of numbers as argument.
Using a for loop, iterate through the list.
For each number, print “bigger” if it’s bigger than 5, “smaller” if it’s smaller than 5, and “equal” if it’s equal to 5
'''


def check_each(list:list[int]):
    for num in list:
        if num < 5:
            print(f"{num} is smaller than 5")
        elif num > 5:
            print(f"{num} is bigger than 5")
        else:
            print(f"{num} is equal to 5")

    return



check_each([2,24,42,64,99,1120,78,98,1000])
        