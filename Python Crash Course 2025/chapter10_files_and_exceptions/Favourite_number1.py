# Write a program that prompts for the user's favorite number. Use json.dumps() 
# to store this number in a file. Write a separate program that reads in this 
# value and prints the message, "I know your favorite number! It's _____."

from pathlib import Path
import json # JavaScript Object Notation
# import the json module

number = input("What's your favourite number? ") 
# user input for a number which we will store for later

path = Path('10.11 favourite_number.json')
# filepath for where the data will be stored
contents = json.dumps(number)
# this will store the the information
path.write_text(contents)

print("Thanks! I'll remember that number.")