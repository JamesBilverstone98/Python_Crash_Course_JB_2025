# An ice cream stand is a specific kind of restaurant. Write a class called 
# IceCreamStand that inherits from the Restaurant class you wrote in Exercise 
# 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class will 
# work; just pick the one you like better. Add an attribute called flavors that 
# stores a list of ice cream flavors. Write a method that displays theese 
# flavors. Create an instance of IceCreamStand, and call this method.

class Restaurant:  # Define the class "Restaurant"
    # Class names should be capitalised by convention

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize the restaurant with a name and cuisine type.
        'self' refers to the specific instance being created.
        """
        self.restaurant_name = restaurant_name.title()  # Store the name with title case
        self.cuisine_type = cuisine_type.title()        # Store the cuisine type
        self.number_served = 0  # Default number of customers served

    def describe_restaurant(self):  # Method to describe the restaurant
        print(f"\n{self.restaurant_name} is a lovely restaurant!")
        print(f"{self.cuisine_type} food is the type of food they sell there.")

    def open_restaurant(self):  # Method to indicate the restaurant is open
        print(f"\n{self.restaurant_name} is now open.")
        print(f"We have served {self.number_served} customers tonight.")

    def set_number_served(self, customers):  # Method to manually set customers served
        self.number_served = customers

    def increment_number_served(self, customers):  # Method to add to the customer count
        self.number_served += customers


# Subclass that inherits from the Restaurant class
class IceCreamStand(Restaurant):  
    # This class is a special kind of Restaurant

    def __init__(self, name, cuisine_type='ice cream'):
        """
        Initialize an IceCreamStand.
        Calls the parent class __init__ using super().
        Sets default cuisine_type to 'ice cream'.
        """
        super().__init__(name, cuisine_type)  # Inherit from Restaurant
        self.flavours = []  # New attribute specific to IceCreamStand

    def show_flavours(self):  # Method to list available flavours
        print("\nWe have the following flavours available:")
        for flavour in self.flavours:
            print(f"- {flavour.title()}")  # Format each flavour nicely


# Create an instance of IceCreamStand
ice_cream = IceCreamStand('Ice Cream Stand')

# Set a list of flavours
ice_cream.flavours = ['vanilla', 'chocolate', 'strawberry']

# Call methods to display the restaurant and its flavours
ice_cream.describe_restaurant()  # Inherited method
ice_cream.show_flavours()        # New method from IceCreamStand
