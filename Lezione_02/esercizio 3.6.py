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