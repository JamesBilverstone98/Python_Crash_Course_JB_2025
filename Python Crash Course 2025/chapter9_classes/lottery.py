from random import choice  # Importing only the 'choice' function to randomly select items from a list

def get_winning_ticket(possibilities):
    """Generate a unique 4-item winning ticket from the list of possibilities."""
    winning_ticket = []

    # Keep adding random, non-repeating items until we have 4
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        # Ensure no duplicate values are added
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    """
    Check if all elements in the played ticket match any in the winning ticket.
    The order doesn't matter, only presence of items.
    """
    for element in played_ticket:
        if element not in winning_ticket:
            return False  # If even one item is not in the winning ticket, it's a losing ticket

    return True  # All items are present, so it's a winner

def make_random_ticket(possibilities):
    """Generate a random ticket of 4 unique items from possibilities."""
    ticket = []
    while len(ticket) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in ticket:
            ticket.append(pulled_item)
    return ticket


# List of possible numbers and letters
possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# Generate the winning combination
winning_ticket = get_winning_ticket(possibilities)

# Start tracking the number of attempts to win
plays = 0
won = False

# Prevent infinite loops by setting a maximum number of attempts
max_tries = 1_000_000

# Try until we win or reach the maximum number of tries
while not won:
    new_ticket = make_random_ticket(possibilities)  # Generate a new random ticket
    won = check_ticket(new_ticket, winning_ticket)  # Check if this ticket is a winner
    plays += 1

    if plays >= max_tries:
        break  # Stop if we've hit the max tries

# Display the result
if won:
    print("🎉 We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays:,} tries to win!")  # Adds commas to the number for readability
else:
    print(f"😢 Tried {plays:,} times, without pulling a winner.")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
