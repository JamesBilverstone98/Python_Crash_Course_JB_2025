# STRIPPING NAMES = use a variable to represent a person's name, and include 
# some whitespace at the beginning and the end of it. 
# Print out the name using the stripping methods

name = " James Bilverstone "

print("\tJames \nBilverstone") # print with a tab, then surname on newline
print(name) # with whitespace
print(name.lstrip()) # with whitespace on the left removed
print(name.rstrip()) # with whitespace on the right removed
print(name.strip()) # all whitespace removed