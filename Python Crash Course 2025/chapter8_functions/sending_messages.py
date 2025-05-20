# SENDING MESSAGES = Start with a copy of your program from Exercise 8-9. 
# Write a function called send_messages() that prints each text message and 
# moves each message to a new list called sent_messages as it’s printed. 
# After calling the function, print both of your lists to make sure 
# the messages were moved correctly.


def show_messages(messages): # passing messages as a paramater to the function
    print("Messages:")
    for message in messages:
        print(message)

def send_messages(unsent_messages, sent_messages):
    print("\nSending all messages:")
    while unsent_messages: # whilst there are items in unsent_messages list
        current_messages = unsent_messages.pop() # add the items to variable
        print(current_messages)
        sent_messages.append(current_messages) # add items to this new list
    
unsent_messages = ['hello', 'how are you', 'goodbye'] # original list
show_messages(unsent_messages)

sent_messages = []
send_messages(unsent_messages, sent_messages)

print("\nFinal lists:")
print(unsent_messages) # shows original list is now empty
print(sent_messages) # new list with items from original list