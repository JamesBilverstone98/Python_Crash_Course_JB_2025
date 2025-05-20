# HELLO ADMIN = make a list of usernames, loop through them and 
# print out certain statements depending on username 

available_usernames = ['james123', 'james98', 'nicole23', 'nicole01', 'admin'] 
# list 1

requested_usernames = ['james1', 'james123', 'nicole123', 'nicole23'] 
# list 2

for requested_username in requested_usernames: # loops through list 2
    if requested_username in available_usernames: 
        # if items from list 2 are in list 1 then print below statement
        print(f"The username {requested_username} is available for use")
    else: # for any items that are not in list 1 then print below statement
        print(f"""The requested username {requested_username}"""
              """ is not available for use""")
        
print("\nPlease log in with your new username") 
# once loop ends, print out this statement on a new line