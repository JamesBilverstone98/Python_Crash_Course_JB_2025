# MESSAGES = Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), which prints each 
# text message.

def show_messages(messages): # passing messages as a paramater to the function
    for message in messages: # loop through the list and print them
        print(message)

messages = ["nice to see you", "how are you?", "goodbye"] # list of messages

show_messages(messages) # calling the function