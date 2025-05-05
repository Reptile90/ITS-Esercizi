class User:
    """Represent a simple user profile."""

    def __init__(self, first_name: str, last_name: str, username: str, email: str) -> None:
        """Initialize the user's personal information."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email

    def describe_user(self) -> None:
        """Display a summary of the user's information."""
        print(f"\nUser: {self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")

    def greet_user(self) -> None:
        """Display a personalized greeting to the user."""
        print(f"Welcome back, {self.username}!")


class Privileges:
    """Represent privileges assigned to an admin user."""

    def __init__(self, privileges: list[str]) -> None:
        """Initialize the privileges."""
        self.privileges = privileges

    def show_privileges(self) -> None:
        """Display the list of privileges."""
        print("Privileges:")
        for privilege in self.privileges:
            print(f" - {privilege}")


class Admin:
    """Represent an admin with user information and privileges."""

    def __init__(self, user: User, privileges: Privileges) -> None:
        """Initialize with a User instance and a Privileges instance."""
        self.user = user
        self.privileges = privileges

    def describe_user(self) -> None:
        """Delegate the user description to the User instance."""
        self.user.describe_user()

    def show_privileges(self) -> None:
        """Delegate the privileges display to the Privileges instance."""
        self.privileges.show_privileges()