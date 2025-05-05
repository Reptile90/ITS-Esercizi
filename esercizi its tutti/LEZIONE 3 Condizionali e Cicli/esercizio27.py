'''6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
Then print each person’s name along with their favorite numbers.'''


favorite_numbers = {
    'Lorenzo': [7,16,22],
    'Patrick': [42,34,66],
    'Giuseppe': [3,45,99],
    'Francesco': [16,98,80],
    'Andrea': [99,23,43]
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for num in numbers:
        print(f"- {num}")
    print("\n")