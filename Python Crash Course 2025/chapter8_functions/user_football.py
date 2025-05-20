# expanding on the code from 8.7 exercise, use a while loop to allow user
# input.

# Define the function to build a footballer profile (first and last name only)
def football_profile(first_name, last_name): 
    """Return a dictionary containing a footballer's name."""
    
    # Create a dictionary with the first and last name
    footballer = {
        'first': first_name.title(),  # Capitalise first letter of first name
        'last': last_name.title(),    # Capitalise first letter of last name
    }
    return footballer  # Return the completed dictionary

# Start an infinite loop to allow repeated user input
while True:
    print("\nPlease tell me your favourite footballer:")
    print("**Press 'q' at any time to quit.**")
    
    # Ask the user for the first name
    first_name = input("\nFirst Name: ")
    if first_name == 'q':  # Check if the user wants to quit
        break
    
    # Ask the user for the last name
    last_name = input("Last Name: ")
    if last_name == 'q':  # Check again for quit command
        break
    
    # Build the dictionary using the function
    player = football_profile(first_name, last_name)
    
    # Show the completed dictionary
    print(player)
    
    