# PIZZA TOPPINGS = write a loop which prompts user for 
# pizza toppings until they quit

while True:
    pizza = input("Please tell me what toppings you would like on the pizza: ") 
    # user input 
    
    if pizza == "quit": # if user says quit, exit program
        break
    else:
        print(f"I will add {pizza} to the pizza") 
        # for all other inputs, print this statement
        
print(f"Your pizza contains all of the requested toppings") 
# once user inputs quit, print this