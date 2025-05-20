# CUBES = make a list of the first 10 cubes 

cubes = [] # empty list

for value in range(1, 11): # loop through numbers 1-10
    cube = value ** 3 # each number in the loop to the power of 3
    cubes.append(cube) # add each cubes value to the cube list

print(cubes) # print out the cubes list once the loop completes


cubes = [value**3 for value in range(1, 11)] 
# list comprehension of the above code
print(cubes) # print out the cubes list once the loop completes