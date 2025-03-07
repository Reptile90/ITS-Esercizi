'''Dinner Guests: Working with one of the programs from Exercises 3, 
use len() to print a message indicating the number of people you’re inviting to dinner.'''

guest_list:list = ["Anthony Kiedis", "John Frusciante", "Michael Balzary", "Chad Smith"]

print(f"Dear {guest_list[0]}, i would be honored to have you join me for a dinner")
print(f"Dear {guest_list[1]}, i would be honored to have you join me for a dinner")
print(f"Dear {guest_list[2]}, i would be honored to have you join me for a dinner")
print(f"Dear {guest_list[3]}, i would be honored to have you join me for a dinner")

print(f"\nI am inviting {len(guest_list)} people to dinner.")