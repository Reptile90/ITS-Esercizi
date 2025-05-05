''' Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.'''

def make_shirt(size='large', message='I love Python'):
    print(f"The shirt size is {size}.")
    print(f"The message printed on the shirt is: {message}")
    print("\n")


make_shirt()


make_shirt(size='medium')


make_shirt(size='small', message='We are Cloud Developer')