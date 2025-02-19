'''More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.'''

guest_list:list = ["Anthony Kiedis", "John Frusciante", "Michael Balzary", "Chad Smith"]

for guest in guest_list:
    print(f"Dear {guest}, i would be honored to have you join me for a dinner")

print("\nUnfortunately, John Frusciante cannot come to dinner.\n")

guest_list[1] = "Dave Navarro"

for guest in guest_list:
    print(f"Dear {guest}, i would be honored to have you join me for a dinner")

print("\nI found a bigger table, so we can invite more people!\n")

guest_list.insert(0,"Misha Mansoor")
guest_list.insert(3, "Mark Holcomb")
guest_list.append("Jake Bowen")

for guest in guest_list:
    print(f"Dear {guest}, i would be honored to have you join me for a dinner")