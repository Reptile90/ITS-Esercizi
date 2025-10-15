from random import randint  # Import the randint function to generate random numbers

class Dice:
    """Represent a dice that can be rolled."""

    def __init__(self, sides: int = 6) -> None:
        """
        Initialize the dice with a specific number of sides.

        Args:
            sides (int): Number of sides on the dice (default is 6).
        """
        self.sides = sides  # Store the number of sides

    def roll_dice(self) -> int:
        """
        Simulate rolling the dice and return a random number.

        Returns:
            int: A random number between 1 and the number of sides.
        """
        return randint(1, self.sides)


# Create a 6-sided dice and show the results of 10 rolls
d6 = Dice()  # Instance of a 6-sided dice

results: list[int] = []  # List to store the results
for roll_num in range(10):
    result = d6.roll_dice()  # Roll the dice
    results.append(result)  # Append the result to the list
print("10 rolls of a 6-sided dice:")
print(results)  # Print the results

# Create a 10-sided dice and show the results of 10 rolls
d10 = Dice(sides=10)  # Instance of a 10-sided dice

results = []
for roll_num in range(10):
    result = d10.roll_dice()
    results.append(result)
print("\n10 rolls of a 10-sided dice:")
print(results)

# Create a 20-sided dice and show the results of 10 rolls
d20 = Dice(sides=20)  # Instance of a 20-sided dice

results = []
for roll_num in range(10):
    result = d20.roll_dice()
    results.append(result)
print("\n10 rolls of a 20-sided dice:")
print(results)