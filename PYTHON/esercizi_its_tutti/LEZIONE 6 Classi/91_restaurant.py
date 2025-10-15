class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, name: str, cuisine_type: str) -> None:
        """
        Initialize the restaurant with a name and cuisine type.

        Args:
            name (str): The name of the restaurant.
            cuisine_type (str): The type of cuisine the restaurant offers.
        """
        self.name = name.title()  # Capitalize the restaurant name
        self.cuisine_type = cuisine_type  # Store the cuisine type

    def describe_restaurant(self) -> None:
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."  # Create the description message
        print(f"\n{msg}")  # Print the message

    def open_restaurant(self) -> None:
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"  # Create the open message
        print(f"\n{msg}")  # Print the message

restaurant = Restaurant('the mean queen', 'pizza')  # Create an instance of the Restaurant class
print(restaurant.name)  # Print the restaurant's name
print(restaurant.cuisine_type)  # Print the restaurant's cuisine type

restaurant.describe_restaurant()  # Display the restaurant description
restaurant.open_restaurant()  # Display that the restaurant is open