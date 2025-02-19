'''Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.'''

guest_list:list[str] = ["Anthony Kiedis", "John Frusciante", "Michael Balzary", "Chad Smith"]


print(f"Dear {guest_list[0]}, i would be honored to have you join me for a dinner")
print(f"Dear {guest_list[1]}, i would be honored to have you join me for a dinner")
print(f"Dear {guest_list[2]}, i would be honored to have you join me for a dinner")
print(f"Dear {guest_list[3]}, i would be honored to have you join me for a dinner")

print("\nUnfortunately, John Frusciante cannot come to dinner.\n")

guest_list[1] = "Dave Navarro"

print(f"Dear {guest_list[0]}, i would be honored to have you join me for a dinner")
print(f"Dear {guest_list[1]}, i would be honored to have you join me for a dinner")
print(f"Dear {guest_list[2]}, i would be honored to have you join me for a dinner")
print(f"Dear {guest_list[3]}, i would be honored to have you join me for a dinner")
