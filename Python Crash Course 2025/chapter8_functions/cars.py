# CARS = Write a function that stores information about a car in a dictionary
# the function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments.
# Call the function with the required information and two other name-value pairs
# such as a color or an optional feature.

# Define a function that builds a dictionary of car information
# 'manufacturer' and 'model' are required arguments
# '**extras' allows the function to accept any number of additional keyword arguments
def make_car(manufacturer, model, **extras):
    """Start building the dictionary with the required information"""
    car_profile = {
        'manufacturer': manufacturer.upper(),  # manufacturer name to uppercase
        'model': model.title(),                # Capitalise the model 
    }

    # Add all other keyword arguments to the dictionary
    for extra, value in extras.items():
        car_profile[extra] = value  # Each key-value pair is added to the car_profile

    return car_profile  # Return the complete car profile


# Call the function with required and extra info
my_car = make_car('bmw', 'one series', colour='blue', manual=True)

# Print the resulting dictionary
print(my_car)