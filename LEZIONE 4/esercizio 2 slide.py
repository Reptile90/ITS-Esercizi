'''Write a function check_length(), which takes a string as an argument.
Using if / else, check if the length of the string is bigger, smaller, or equal to 10 characters'''

def check_lenght(string:str):
    if len(string) < 10:
        print(f"the string \"{string}\" length is smaller than 10 characters")
    elif len(string) >10:
        print(f"the string \"{string}\" length is bigger than 10 characters")
    else:
        print(f"the string \"{string}\" lenght is equal to 10 characters")
    return


check_lenght("ciao ")