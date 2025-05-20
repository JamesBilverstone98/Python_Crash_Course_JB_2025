from random import randint  # Importing a function that generates random integers

class Die:
    """Represent a die, which can be rolled."""
    
    def __init__(self, sides=6):
        """Initialize the die with a default of 6 sides."""
        self.sides = sides  # Save the number of sides to an instance variable

    def roll_die(self):
        """Simulate rolling the die: return a random number between 1 and the number of sides."""
        return randint(1, self.sides)  # Roll and return a random side

# ---------------------------
# Roll a 6-sided die 10 times
# ---------------------------
d6 = Die()  # Create a die object with default 6 sides

results = []  # List to store the results
for roll_num in range(10):  # Loop 10 times
    result = d6.roll_die()  # Roll the die
    results.append(result)  # Add the result to the list
print("10 rolls of a 6-sided die:")
print(results)  # Show all results

# ---------------------------
# Roll a 10-sided die 10 times
# ---------------------------
d10 = Die(sides=10)  # Create a die object with 10 sides

results = []  # Reset the results list
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

# ---------------------------
# Roll a 20-sided die 10 times
# ---------------------------
d20 = Die(sides=20)  # Create a die object with 20 sides

results = []  # Reset the results list again
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)