# MY PIZZAS, YOUR PIZZAS = copy a list and add things to it

my_foods = ['pizza', 'chicken', 'chips']
nicoles_foods = my_foods[:] 
# this copies the list from my_foods and passes it to nicoles_foods variable

my_foods.append('chocolate') # adding item to original list
nicoles_foods.append('sweets') # we can also add items to the copied list

print("\nMy favourite foods are:")
print(my_foods) # prints out my_foods list

print("\nNicole's favourite foods are:")
print(nicoles_foods) 
# prints out the newly formed list which had been copied from my_foods

print("\nMy favourite foods are:")
for food in my_foods: # loop through the items in my_foods
    print(food)