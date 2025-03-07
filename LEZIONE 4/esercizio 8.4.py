'''Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.'''


def make_shirt(size="Large", message= "I love Python"):

    print(f"I would buy a {size} t-shirt with the message \"{message}\"")

    


make_shirt("XL", "I'm a software developer")


make_shirt(size="XL", message = "I'm a software developer")


make_shirt()

make_shirt("medium")
