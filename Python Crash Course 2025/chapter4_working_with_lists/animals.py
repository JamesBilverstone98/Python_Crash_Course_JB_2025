# ANIMALS = think of a few different animals, print them out using for loop.

animals = ['dog', 'cat', 'hamster', 'parrot']

for animal in animals: # for every item in the list, assign it to animal variable
    print(animal)
    
for animal in animals:
    print(f"\nA {animal} would make a great pet") # loops through all items 
    # in the list

print(f"\nI love having a {animals[0]} and {animals[1]} the best") 
# then prints this statement once the loop has finished, picking the first
# and second items via indexing
