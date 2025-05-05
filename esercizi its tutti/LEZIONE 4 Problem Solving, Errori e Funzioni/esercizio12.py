'''Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. 
Call the function three times, using a different number of arguments each time.'''

def make_sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
    print("Enjoy your sandwich!")


make_sandwich('turkey', 'lettuce', 'tomato', 'mayo')
make_sandwich('ham', 'cheese')
make_sandwich('peanut butter', 'jelly')