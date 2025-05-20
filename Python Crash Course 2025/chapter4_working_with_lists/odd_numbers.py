# ODD NUMBERS = use the third argument of the range function 
# to make a list of the odd numbers from 1-20, using a for loop

odd_numbers = list(range(1, 21, 2)) # range starts from 1, through to 20, 
# adding 2 to each number, then adding them all to a list
print(odd_numbers)

for number in odd_numbers:  
    # using a for loop to print the odd numbers from 1-20
    print(number)