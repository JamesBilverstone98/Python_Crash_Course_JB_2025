# CITY NAMES = write a function called city_country that takes in the name
# of a city and country. Call the function with 3 city-country pairs


def city_country(city, country): # defining function with 2 paramaters
    print(f"{city.title()}, {country.upper()}")
    # prints first argument with first letter capitalised and other uppercase
    
city_country('newcastle', 'england') # calling function 
city_country('paris', 'france') # calling function 
city_country('rome', 'italy') # calling function 