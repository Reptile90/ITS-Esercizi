'''Do the following to create a program that simulates how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing user'''


current_users:list[str] = [
    "lorenzo", 
    "giuseppe", 
    "patrick", 
    "francesco", 
    "giulia"
    ]
new_users:list[str] = [
    "demis", 
    "liridon", 
    "deyan", 
    "francesco", 
    "ivan"
    ]

copy_users:list[str] = current_users.copy()

for user in copy_users:
    user.lower()

for user in new_users:
    if user.lower() in copy_users:
        print(f"Sorry, the username '{user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{user} is available.")