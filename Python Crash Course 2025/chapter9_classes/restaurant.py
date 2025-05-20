# RESTAURANT = Make a class called Restaurant. The __init__() method for 
# Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of 
# information, and a method called open_restaurant() that prints a message 
# indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes 
# individually, and then call both methods.

class Restaurant:  # Define the class (class names should use TitleCase)
    
    def __init__(self, restaurant_name, cuisine_type):
        """
        The __init__ method is called automatically when a new object is created.
        'self' refers to the instance itself.
        """
        self.restaurant_name = restaurant_name.title()  # Store name, formatted with title case
        self.cuisine_type = cuisine_type.title()        # Store cuisine type, also title-cased
        self.number_served = 0  # Default value for customers served (starts at 0)

    def describe_restaurant(self):
        """Prints a description of the restaurant."""
        print(f"\n{self.restaurant_name} is a lovely restaurant!")
        print(f"{self.cuisine_type} food is the type of food they sell there")

    def open_restaurant(self):
        """Indicates the restaurant is open and shows how many customers have been served."""
        print(f"\n{self.restaurant_name} is now open.")
        print(f"We have served {self.number_served} customers tonight.")

    def set_number_served(self, customers):
        """
        Allows setting the number of customers served directly.
        Useful for updating data (e.g., loading from a file or resetting).
        """
        self.number_served = customers

    def increment_number_served(self, customers):
        """
        Adds to the number of customers served.
        Useful for tracking daily increases or new visitors.
        """
        self.number_served += customers


# Create an instance (object) of the Restaurant class with specific name and cuisine
favourite_restaurant = Restaurant('babuchos', 'italian')

# Access and print the stored attributes directly
print(favourite_restaurant.restaurant_name)  # Output: Babuchos
print(favourite_restaurant.cuisine_type)     # Output: Italian

# Call method to describe the restaurant
favourite_restaurant.describe_restaurant()

# Call method to show it's open and how many customers have been served
favourite_restaurant.open_restaurant()

# Set the number of customers to a specific number
favourite_restaurant.set_number_served(50)
favourite_restaurant.open_restaurant()

# Increment the number served by an additional 100 customers
favourite_restaurant.increment_number_served(100)
favourite_restaurant.open_restaurant()
