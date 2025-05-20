# SLICES = print out numerous statements using the 
# slicing methods previously covered

names = ['nicole', 'woody', 'james', 'scarlett', 'callie']

print("The first 3 names in this list are:")
for name in names[:3]: # loops through the first 3 names
    print(name.title()) # prints out the first 3 names with first 
    # letter being capitalised
    
print("\nThe middle 3 names in this list are:")
for name in names[1:4]: # loops through the middle 3 names
    print(name.title()) # prints out the middle 3 names with the first 
    # letter being capitalised
    
print("\nThe last 3 names in this list are:")
for name in names[-3:]: # loops through the last 3 names
    print(name.title()) # prints out the last 3 names with the first 
    # letter being capitalised