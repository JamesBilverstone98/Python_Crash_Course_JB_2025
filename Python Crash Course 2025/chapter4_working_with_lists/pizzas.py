# PIZZAS = list pizzas, use for loop to print them

pizzas = ['ham', 'pepperoni', 'meatfeast', 'bbq chicken']

for pizza in pizzas: # for every item in the list, assign it to a variable 
    # called pizza
    print(pizza)

for pizza in pizzas:
    print(f"\nI like {pizza} pizzas") # this loops through the list until 
    # it has printed a statement out for all items
    
print(f"\nI like {pizzas[0]} pizzas the best though") # this statement then 
# prints once the for loop has finished as it is outside of the loop
# picks the first item in the list due to 0 indexing
    