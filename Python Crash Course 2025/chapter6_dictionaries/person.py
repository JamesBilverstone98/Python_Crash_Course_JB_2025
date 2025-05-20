# PERSON = use a dictionary to store information and then 
# print out each key-value pair

profile = {'first_name': 'james', 
           'last_name': 'bilverstone', 
           'city': 'newcastle', 
           'age': 26,
           } # dictionary containing 4 key-value pairs

print(profile['first_name']) # prints value assigned to first_name key
print(profile['last_name']) # prints value assigned to last_name key
print(profile['city']) # prints value assigned to city key
print(profile['age']) # prints value assigned to age key

print(f"""\n{profile['first_name'].title()}' last name is """
      f"""{profile['last_name'].title()}, he is {profile['age']} years old """
      f"""and lives in {profile['city'].upper()}""")