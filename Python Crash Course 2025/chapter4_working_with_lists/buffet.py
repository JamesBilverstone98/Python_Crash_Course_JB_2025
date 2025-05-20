# BUFFET = store foods in a tuple, print them out using for loop.
# menu changes with items being replaced, print out new menu using for loop

menu = ('pizza', 'chicken', 'chips', 'burgers', 'garlic bread')

print("\nOriginal Menu:")
for item in menu: # loops through the tuple 
    print(item.title()) 
    # prints out each tuple item with first letter capitalised
  
menu = ('pizza', 'chicken nuggets', 'cheesy chips', 'cheeseburgers', 
        'potato skins') # amended original tuple
print("\nNew Menu:")
for item in menu: # loops through the new tuple
    print(item.title()) 
    # prints out each new tuple item with first letter capitalised