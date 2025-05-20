# RIVERS = make a dictionary containing 3 major rivers and 
# the countries they run through, use loop to run through them

rivers = { # dictionary
    'nile': 'egypt',
    'amazon': 'brazil',
    'the thames': 'england',
    }

print(rivers['nile'].upper()) 
# prints out the value assigned to the nile key in uppercase
print(rivers['amazon'].upper()) 
# prints out the value assigned to the amazon key in uppercase
print(rivers['the thames'].upper()) 
# prints out the value assigned to the thames key in uppercase


print(f"\nThe Nile runs through {rivers['nile'].title()}") 
# prints out the value assigned to the nile key with first letter capitalised
print(f"The Amazon runs through {rivers['amazon'].title()}") 
# prints out the value assigned to the amazon key with first letter capitalised
print(f"The Nile runs through {rivers['the thames'].title()}") 
# prints out the value assigned to the thames key with first letter capitalised


for key, value in rivers.items(): 
# loops through the dictionary and assigns the keys-value pairs to 
# key variable and value variable
    print(f"\nDictionary Keys: {key.title()}") 
    # prints out the keys in the dictionary
    print(f"Dictionary Values: {value.title()}") 
    # prints out the values in the dictionary

print("\n")
   
for river in sorted(rivers): 
    # loops through the keys in alphabetical order
    print(f"The {river.upper()} is huge")

print("\n")

for river in sorted(rivers.values()): 
    # loops through the values in alphabetical order
    print(f"The values of the dictionary are: {river.title()}")
    

    
    