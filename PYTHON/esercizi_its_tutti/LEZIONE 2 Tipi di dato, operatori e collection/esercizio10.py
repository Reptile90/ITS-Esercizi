'''3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.'''


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



















