'''Dinner Guests: Working with one of the programs from Exercises 3, 
use len() to print a message indicating the number of people you’re inviting to dinner.'''

guest_list:list = ["Anthony Kiedis", "John Frusciante", "Michael Balzary", "Chad Smith"]

for guest in guest_list:
    print(f"Dear {guest}, i would be honored to have you join me for a dinner")

    print(f"\nI am inviting {len(guest_list)} people to dinner.")