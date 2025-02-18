guest_list:list = ["Anthony Kiedis", "John Frusciante", "Michael Balzary", "Chad Smith"]

for guest in guest_list:
    print(f"Dear {guest}, i would be honored to have you join me for a dinner")

print("\nUnfortunately, John Frusciante cannot come to dinner.\n")

guest_list[1] = "Dave Navarro"

for guest in guest_list:
    print(f"Dear {guest}, i would be honored to have you join me for a dinner")
