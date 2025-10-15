'''3-9. Dinner Guests: Working with one of the programs from Exercises 3, use len() to print a message indicating the number of people you’re inviting to dinner
'''


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


print(f"i invite {len(invite)} person")