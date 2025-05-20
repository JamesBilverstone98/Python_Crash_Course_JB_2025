# CITIES = write a function called describe_city, that accepts the name 
# of a city and its country


# calling the function with a default value for country
def describe_city(city, country='uk'): 
    """City and the country they are in""" 
    print(f"{city.title()} is not in the {country.upper()}, it is in Europe.")
    
describe_city('barcelona') # passing through an argument for city only
describe_city('rome') # passing through an argument for city only
describe_city('paris') # passing through an argument for city only