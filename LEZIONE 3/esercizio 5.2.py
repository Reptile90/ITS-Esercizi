'''More Conditional Tests: You don’t have to limit the number of tests you cre-
ate to 10. If you want to try more comparisons, write more tests and add them

to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list'''

name:str = 'Stefano'
print("\nIs name == 'Stefano'? I predict True.")
print(name == 'Stefano')
print("\nIs name == 'Marcel'? I predict False.")
print(name == 'Marcel')


name:str = 'Stefano'
print("\nIs name == 'Stefano'? I predict True.")
print(name == 'Stefano')
print("\nIs name == 'marcel'? I predict False.")
print(name == 'Marcel'.lower)


number:int = 3
print("\nIs number == 3? I predict True.")
print(number == 3)
print("\nIs number == 6? I predict False.")
print(number == 6)

number1:int = 3
number2:int = 6

print("\nIs numbers == 3 and 6 is greater than 1 and 2? I predict True.")
print(number1 == 3 and number2 == 6)
print("\nIs numbers == 1 and 2 is greater than 3 and 6? I predict False.")
print(number1 == 1 and number2 == 2 )


print("\nIs numbers == 3 or 6 is greater than 1 or 2? I predict True.")
print(number1 == 3 or number2 == 6)
print("\nIs numbers == 1 or 2 is greater than 3 or 6? I predict False.")
print(number1 == 1 or number2 == 2 )


lista:list[str] = ["a","b","c","d"]

print("\nIs list contain a? I predict True.")
print("a"in (lista))
print("\nIs list contain e? I predict False.")
print("e"in (lista))
