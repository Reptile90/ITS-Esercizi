'''You don’t have to limit the number of tests you cre-
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

fruit = 'apple'
print("Is fruit == 'apple'? I predict True.")
print(fruit == 'apple')

print("\nIs fruit != 'orange'? I predict True.")
print(fruit != 'orange')

print("\nIs fruit == 'banana'? I predict False.")
print(fruit == 'banana')

print("\nIs fruit != 'apple'? I predict False.")
print(fruit != 'apple')

name = 'John Doe'
print("\nIs name.lower() == 'john doe'? I predict True.")
print(name.lower() == 'john doe')

print("\nIs name.lower() == 'JOHN DOE'? I predict False.")
print(name.lower() == 'JOHN DOE')

age = 25
print("\nIs age == 25? I predict True.")
print(age == 25)

print("\nIs age != 30? I predict True.")
print(age != 30)

print("\nIs age > 20? I predict True.")
print(age > 20)

print("\nIs age < 30? I predict True.")
print(age < 30)

print("\nIs age >= 25? I predict True.")
print(age >= 25)

print("\nIs age <= 25? I predict True.")
print(age <= 25)

print("\nIs age == 30? I predict False.")
print(age == 30)

print("\nIs age != 25? I predict False.")
print(age != 25)

print("\nIs age > 30? I predict False.")
print(age > 30)

print("\nIs age < 18? I predict False.")
print(age < 18)

print("\nIs age >= 30? I predict False.")
print(age >= 30)

print("\nIs age <= 20? I predict False.")
print(age <= 20)