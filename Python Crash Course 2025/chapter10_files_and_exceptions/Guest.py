# GUEST = Write a program that prompts the user for their name. 
# When they respond, write their name to a file called guest.txt.

from pathlib import Path

path = Path("guest.txt") # this is the name of the txt file where the user input
# will go

name = input("What is your name? ")
path.write_text(name) # user input name is written to the txt file