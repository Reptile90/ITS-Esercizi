'''4-2. Animals: Think of at least three different animals that have a common characteristic. 
Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
• Modify your program to print a statement about each animal, such as A dog would make a great pet.
• Add a line at the end of your program, stating what these animals have in common. 
You could print a sentence, such as Any of these animals would make a great pet
'''


animals = [
    "Lion", "Tiger", "Elephant", "Giraffe", "Bear", "Kangaroo", "Koala", "Panda", "Wolf", "Deer",
    "Eagle", "Hawk", "Penguin", "Shark", "Dolphin", "Whale", "Hippo", "Rhino", "Zebra", "Horse",
    "Cow", "Sheep", "Goat", "Pig", "Rabbit", "Mouse", "Squirrel", "Hedgehog", "Lynx", "Leopard",
    "Cat", "Dog", "Fox", "Hyena", "Chameleon", "Anaconda", "Crocodile", "Turtle", "Alligator", "Owl",
    "Barn Owl", "Parrot", "Ferret", "Earthworm", "Spider", "Snake", "Cricket", "Dragonfly", "Fly", "Butterfly",
    "Horsefly", "Moth", "Beetle", "Ant", "Grasshopper", "Ladybug", "Cockroach", "Termite", "Flea", "Mosquito",
    "Bat", "Cheetah", "Jaguar", "Snow Leopard", "Otter", "Seal", "Walrus", "Platypus", "Armadillo", "Raccoon",
    "Skunk", "Possum", "Mole", "Weasel", "Ferret", "Bison", "Buffalo", "Camel", "Alpaca", "Llama",
    "Peacock", "Pheasant", "Turkey", "Chicken", "Goose", "Duck", "Swan", "Crow", "Raven", "Vulture",
    "Falcon", "Robin", "Woodpecker", "Wren", "Swallow", "Stork", "Kingfisher", "Sparrow", "Hummingbird", "Starling"
]


for name in animals:
    if name == "Dog":
        print(f"A {name} would make a great pet")
    else:
        print(f"A {name} would make a great animals")