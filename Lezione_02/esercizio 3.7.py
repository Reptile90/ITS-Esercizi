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