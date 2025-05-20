# FAVOURITE PLACES = make a dictionary and include peoples 
# names and favourite places

favourite_places = { # dictionary
    'james': 'florida',
    'nicole': 'malaga',
    'woody': 'backgarden',
    }

for key, value in favourite_places.items(): 
    # assigning keys-values pairings to key and value variables
    print(f"Keys: {key.title()}") 
    # prints out the keys with first letter capitalised
    print(f"Values: {value.upper()}") 
    # prints out the values with first letter capitalised
 
print("\n")   
for name in sorted(favourite_places): 
    # loops through the names in dictionary in alphabetical order
    print(f"{name}, what is your favourite destination?")
 

print("\n")   
for name in sorted(favourite_places):
    print(f"The values are: {name.title()}")
    
