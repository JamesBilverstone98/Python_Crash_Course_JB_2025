# SEEING THE WORLD = using 5 places in the world, print them out using
# numerous different list organisational methods

locations = ['rome', 'venice', 'oslo', 'copenhagen', 'florida', 'berlin', 
             'krakow']

print(locations)

print("\n")
locations.sort() # sorts the locations in alphabetical order
print(locations)

locations.sort(reverse=True) # sorts the locations in reverse alphabetical order
print("\n")
print(locations)


print("\n")
print(len(locations)) # counts the amount of items in the list

print("\n")
print(f"There are {len(locations)} locations in your list")