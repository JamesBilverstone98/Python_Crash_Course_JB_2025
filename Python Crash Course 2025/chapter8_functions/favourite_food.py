# FAVOURITE FOOD = write a function which prints out favourite food and 
# also use argument and paramater

def favourite_food(name, food): # defining the function with two paramaters
    """Favourite food items belonging to individual"""
    print(f"\n{name.title()}, your favourite food is {food.upper()}!\n")
    

favourite_food('james', 'ham pizza') # calling the function with two arguments 
favourite_food('nicole', 'steak') 
# calling the function again but with two different arguments