# GUEST LIST = make a list of at least 3 people then print a message to each 
# person

guest_list = ['nicole', 'neil armstrong', 'woody'] # list

print(f"{guest_list[0].upper()}, you are my girlfriend") # uppercases the first 
# item in the list
print(f"{guest_list[1].title()}, are aliens real?") # capitalises the first 
# letters in the item words indexed at the 2nd item

popped_name = guest_list.pop() # removes the last item in the list and 
# assigns it to a variable
print(f"{popped_name.title()}, you are a cat") # print out the new variable

guest_list.insert(0, 'callie') # replaces first item in the list
print(f"{guest_list[0].title()}, you have been added to the list")

guest_list.append('james') # adds item to the end of the list
print(guest_list)

del guest_list[-1] # deletes the last item from the list due to -1 index
print(guest_list)

