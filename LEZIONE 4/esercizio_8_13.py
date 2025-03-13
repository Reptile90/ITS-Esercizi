'''User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you. All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"'''

def build_profile(first_name:str, last_name:str, age:str, hair:str, car:str):
    profile:str = f"    {first_name} {last_name}, Age: {age}, Hair: {hair}, Car: {car}"

    return profile


print(build_profile("Stefano", "Reali", "45", "Brown", "Peugeot 207"))
