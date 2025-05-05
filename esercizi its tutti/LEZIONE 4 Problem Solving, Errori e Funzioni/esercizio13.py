'''User Profile:  
Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you. 
All the values must be passed to the function as parameters. 
The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"'''

def build_profile(first_name,last_name, age, hair, height)->str:
        return f"{first_name} {last_name}, Age: {age}, Hair: {hair},  Height: {height}"


print(build_profile("Stefano", "Reali", 34, "Brown", "193 cm"))