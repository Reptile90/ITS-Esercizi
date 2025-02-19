'''Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. 
  Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. 
Print your list to make sure you actually have an empty list at the end of your program.'''

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


print("\nUnfortunately, the new dinner table won't arrive in time, and I can invite only two people to dinner.\n")

while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Sorry, {removed_guest}, but I can't invite you to dinner.")

for guest in guest_list:
    print(f"Dear {guest}, you are still invited to dinner.")

del guest_list[:]
print(f"\nFinal guest list: {guest_list}")