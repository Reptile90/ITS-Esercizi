'''Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed for the appropriate color alien.'''

alien_colour:str= "red"

if alien_colour == "green":
    print("You've earned 5 points for shooting the alien")
elif alien_colour == "yellow":
    print("You've earned 10 points for shooting the alien")
else:
    print("You've earned 15 points")


alien_colour:str= "yellow"

if alien_colour == "green":
    print("You've earned 5 points for shooting the alien")
elif alien_colour == "yellow":
    print("You've earned 10 points for shooting the alien")
else:
    print("You've earned 15 points")

alien_colour:str= "green"

if alien_colour == "green":
    print("You've earned 5 points for shooting the alien")
elif alien_colour == "yellow":
    print("You've earned 10 points for shooting the alien")
else:
    print("You've earned 15 points")