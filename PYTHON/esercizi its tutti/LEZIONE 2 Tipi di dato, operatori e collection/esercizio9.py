'''Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.'''


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
