# FOOTBALL = write a function called football_profile that builds a 
# dictionary. Use the function to make 3 dictionaries and print each return
# value. Use None to add an optional paramater


# Define the function with required parameters and an optional one (age)
def football_profile(first_name, last_name, football_club, age=None):
    """Build a dictionary containing details about a footballer."""
    
    # Create a dictionary with the footballer's name and club
    footballer = {
        'first': first_name.title(),  # Capitalise first name
        'last': last_name.title(),    # Capitalise last name
        'club': football_club.upper() # Make club name uppercase
    }
    
    # Only add 'age' to the dictionary if it's provided
    if age:
        footballer['age'] = age
    
    # Return the full footballer profile dictionary
    return footballer

# Create several footballer dictionaries using the function
footballer1 = football_profile('lionel', 'messi', 'inter miami')  
footballer2 = football_profile('eden', 'hazard', 'retired')       
footballer3 = football_profile('cole', 'palmer', 'chelsea')       
footballer4 = football_profile('cristian', 'ronaldo', 'al nassr', 38)  

# Print each dictionary to see the results
print(footballer1)
print(footballer2)
print(footballer3)
print(footballer4)