'''Safe Square Root: Write a function safe_sqrt(number) that calculates the square root of a number using math.sqrt(). Handle ValueError if the input is negative by returning an informative message.'''

import math
def safe_sqrt(number)->float:
    try:
        
        print(math.sqrt(number))

    except ValueError as error:
        print(error)
        print(f"The number must be positive")
        




(safe_sqrt(-1))
