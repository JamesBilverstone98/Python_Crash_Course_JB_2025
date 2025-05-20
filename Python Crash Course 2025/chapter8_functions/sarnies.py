# SARNIES = write a function that accepts a list of items a person wants on a   
# sandwich. The function should have one parameter that collects as many items
# as the function call provides, and it should print a summary of the sarnie
# that is being orders. Call the function three times using a different number
# of arguments each time

def sarnies(*toppings): # telling Python we are unsure how many arguments
# will be passed to the toppings parameter
    print(f"\nThe following toppings have been added to your order:")
    for topping in toppings: # loop through any arguments which are passed
        print(f"{topping}")

sarnies('ham') 
sarnies('ham', 'cheese')
sarnies('ham', 'chicken', 'bacon')
# all of these work as we told Python that an arbitrary number of arguments
# will be passed when defining the function




 
