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
        self.number_served = 0  # Initialize number of customers served

    def describe_restaurant(self) -> None:
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."  # Create the description message
        print(f"\n{msg}")  # Print the message

    def open_restaurant(self) -> None:
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"  # Create the open message
        print(f"\n{msg}")  # Print the message

    def set_number_served(self, number_served: int) -> None:
        """
        Allow user to set the number of customers that have been served.

        Args:
            number_served (int): The number of customers served.
        """
        self.number_served = number_served  # Set the number served

    def increment_number_served(self, additional_served: int) -> None:
        """
        Allow user to increment the number of customers served.

        Args:
            additional_served (int): Number of additional customers served.
        """
        self.number_served += additional_served  # Increment the number served


# Create an instance of Restaurant and demonstrate functionality
restaurant = Restaurant('the mean queen', 'pizza')  # Initialize the restaurant
restaurant.describe_restaurant()  # Describe the restaurant

print(f"\nNumber served: {restaurant.number_served}")  # Print initial number served

restaurant.number_served = 500  # Directly set number served
print(f"Number served: {restaurant.number_served}")  # Print updated number

restaurant.set_number_served(1000)  # Use method to set number served
print(f"Number served: {restaurant.number_served}")  # Print updated number

restaurant.increment_number_served(250)  # Increment the number served
print(f"Number served: {restaurant.number_served}")  # Print final number