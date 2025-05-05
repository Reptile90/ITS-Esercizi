from random import choice  # Import function to randomly select items

class LotteryMachine:
    """A class to simulate a simple lottery machine."""

    def __init__(self) -> None:
        """Initialize the machine with a pool of 10 numbers and 5 letters."""
        self.pool: list[str] = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'a', 'b', 'c', 'd', 'e']  # Combined pool of numbers and letters
        self.winning_ticket: list[str] = []  # List to hold the winning ticket

    def draw_winning_ticket(self) -> None:
        """Randomly select 4 unique items from the pool to create the winning ticket."""
        while len(self.winning_ticket) < 4:
            pulled: str = choice(self.pool)
            if pulled not in self.winning_ticket:
                self.winning_ticket.append(pulled)

    def announce_winner(self) -> None:
        """Display a message with the winning ticket."""
        print("The winning ticket is:", self.winning_ticket)
        print("Any ticket matching these 4 items wins a prize!")


# Create an instance of the LotteryMachine
lottery = LotteryMachine()
lottery.draw_winning_ticket()  # Draw the ticket
lottery.announce_winner()  # Announce the winner
