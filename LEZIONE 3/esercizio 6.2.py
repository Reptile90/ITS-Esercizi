'''Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.'''



favorite_numbers:dict[any]= {"Stefano": 6, "Lorenzo": 3, "Marcel": 12, "Valentina": 4, "Leandro": 1}

for name in favorite_numbers:
    print(f"{name}'s favorite number is: {favorite_numbers[name]}")