'''You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6.
Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list.
Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. 
Print your list to make sure you actually have an empty list at the end of your program.'''


invite:list[str] = ["Anthony Kiedis","John Frusciante","Michael Balzary","Chad Smith"]

print(f"Hey {invite[0]} i would like to invite you to dinner")
print(f"Hey {invite[1]} i would like to invite you to dinner")
print(f"Hey {invite[2]} i would like to invite you to dinner")
print(f"Hey {invite[3]} i would like to invite you to dinner")


print(f"{invite[1]} can't come to dinner with us.")

invite.pop(1)
invite.append("Dave Navarro")

print(f"Hey {invite[3]} i would like to invite you to dinner")

print(invite)

print(f"Hey {invite[0]}, {invite[1]}, {invite[2]}, {invite[3]} i've found a new table. ")

invite.insert(0,"John Frusciante")
invite.insert(3,"Josh Klinghoffer")
invite.append("Hillel Slovak")


print(invite)

print(f"Hey {invite[0]} i would like to invite you to dinner")
print(f"Hey {invite[3]} i would like to invite you to dinner")
print(f"Hey {invite[6]} i would like to invite you to dinner")


print(f"Sorry {", ".join(invite)} the table isn't arrive in time. I can invite only two person")


invite.pop(2)
invite.pop(2)
invite.pop(2)
invite.pop(2)
invite.pop(1)

print(invite)

print(f"{invite[0]}, {invite[1]} you're still invited")

invite.pop(0)
invite.pop(0)


print(invite)





















