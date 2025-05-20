# THREES = make a list of the multiples of 3 (from 3-30)

threes = list(range(3, 31, 3)) # # range starts from 3, through to 30, 
# adding 3 to each number, then adding them all to a list
print(threes)

for three in threes:  
    # using a for loop to print the multiples of 3 up until 30
    print(three)