class User:
    """Represent a simple user profile."""

    def __init__(self, first_name: str, last_name: str, username: str, email: str, location: str) -> None:
        """
        Initialize the user with basic profile information.

        Args:
            first_name (str): The user's first name.
            last_name (str): The user's last name.
            username (str): The user's unique username.
            email (str): The user's email address.
            location (str): The user's location.
        """
        self.first_name = first_name.title()  # Capitalize the first name
        self.last_name = last_name.title()  # Capitalize the last name
        self.username = username  # Store the username
        self.email = email  # Store the email address
        self.location = location.title()  # Capitalize the location

    def describe_user(self) -> None:
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")  # Print full name
        print(f"  Username: {self.username}")  # Print username
        print(f"  Email: {self.email}")  # Print email
        print(f"  Location: {self.location}")  # Print location

    def greet_user(self) -> None:
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")  # Print greeting message


# Create and describe a user named Eric
eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()  # Show Eric's profile information
eric.greet_user()  # Greet Eric

# Create and describe a user named Willie
willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()  # Show Willie's profile information
willie.greet_user()  # Greet Willie