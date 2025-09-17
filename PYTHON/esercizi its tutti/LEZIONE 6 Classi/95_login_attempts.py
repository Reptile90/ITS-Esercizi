class User:
    """Represent a simple user profile."""

    def __init__(self, first_name: str, last_name: str, username: str, email: str, location: str) -> None:
        """
        Initialize the user with profile information and login attempt tracking.

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
        self.login_attempts = 0  # Initialize login attempts counter

    def describe_user(self) -> None:
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")  # Print full name
        print(f"  Username: {self.username}")  # Print username
        print(f"  Email: {self.email}")  # Print email
        print(f"  Location: {self.location}")  # Print location

    def greet_user(self) -> None:
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")  # Print greeting

    def increment_login_attempts(self) -> None:
        """Increment the value of login_attempts by one."""
        self.login_attempts += 1  # Increase login attempts count

    def reset_login_attempts(self) -> None:
        """Reset login_attempts to 0."""
        self.login_attempts = 0  # Reset counter to zero


# Create an instance of the User class
eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()  # Show user's profile
eric.greet_user()  # Greet the user

print("\nMaking 3 login attempts...")
eric.increment_login_attempts()  # First login attempt
eric.increment_login_attempts()  # Second login attempt
eric.increment_login_attempts()  # Third login attempt
print(f"  Login attempts: {eric.login_attempts}")  # Display number of login attempts

print("Resetting login attempts...")
eric.reset_login_attempts()  # Reset login attempts
print(f"  Login attempts: {eric.login_attempts}")  # Display reset value