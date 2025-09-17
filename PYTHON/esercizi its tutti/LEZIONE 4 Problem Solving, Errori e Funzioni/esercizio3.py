'''T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
The function should print a sentence summarizing the size of the shirt and the message printed on it. 
Call the function once using positional arguments to make a shirt. 
Call the function a second time using keyword arguments.'''


def make_shirt(size, message)->None:
    print(f"The shirt size is {size} and it will have the message: '{message}' printed on it.")


make_shirt("M", "Keep calm and code on!")


make_shirt(message="Python is awesome!", size="L")


