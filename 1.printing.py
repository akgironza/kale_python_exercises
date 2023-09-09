
# 1. Using the print method, print "Hello World"
#print('Hello World')

# 2. Create variables for the data type below. 
# Data Types:
# Int
dt_int = 1

# Float
dt_float = 2.0

# String
dt_string = "text"

# Boolean
dt_boolean1 = True

# Boolean (The other boolean value)
dt_boolean2 = False

# Lists ( 4 items in list min.)
dt_list_fruits = ['strawberry', 'banana', 'guava', 'mango', 'blackberry']

# Dictionaries  ( 4 key/value pairs min.)
dt_dictionary_zoe = {"name": "Zoe", 
                     "species": "cat", 
                     "age": "4", 
                     "favorite_treat": "birds"}

# 3. For each of the variables, use the print method for each variable. To print each varible
#print(dt_int)
#print(dt_float)
#print(dt_string)
#print(dt_boolean1)
#print(dt_boolean2)
#print(dt_list_fruits)
#print(dt_dictionary_zoe)

# 4. Backtick ` in JS are used for Template literals. In a JS file a variable called intVariable and stringVariable exist.
# They are equal to the int and string variables on step 2.
# What is the python equvalent for: console.log(`int: ${intVariable}, string ${stringVariable}`)
#print(f"int: {dt_int}, string: {dt_string}")

# 5. Comment out all print statements up to this point


# 6. Write a FOR LOOP in python that prints "David Rocks" 5 times
# Hint: type this into google "loop range python"
#q6_text = "David Rocks"
#for i in range(5):
#    print(q6_text)

# 7. Declare a function what print "Alex Rocks". Invoke that function 5 times. 
#def print_alex_rocks():
#    q7_text = "Alex Rocks"
    
#    for i in range(5):
#        print(q7_text)

#print_alex_rocks()

# 8. Declare a function that takes in 2 parameters. 
# It will print "P1(your parameter1) and P2(your parameter2) Rocks"
# Now call that function using "Kyle" and "Winston" as the arguments 
# invoke that function 4 more times
#def q8_function(P1, P2):
#    print(f"{P1} Rocks")
#    print(f"{P2} Rocks")

#for i in range(4):
#    q8_function("Kyle", "Winston")

# Definitions:  
# P is for Placeholder. P is for Parameters.
# These 2 start w/ the letter P 
# A parameter is variable in the declaration of the function - The place holder

# A is for actual value. A is for aguement.
# These 2 start w/ the letter A
# Arguement is are the values when calling the function - The actual value

# 9. Remember the list variable in step 2. 
# a. Print the index at 3. Then comment it out
#print(dt_list_fruits[3])

# b. Now print the index at 100. Does this error? comment it out
#print(dt_list_fruits[100])
# IndexError: list index out of range

# e. Now print the index at -1 index. Observe what it prints. Then comment it out
#print(dt_list_fruits[-1])

# f. Now print the index at -100.  Does this error? comment it out
#print(dt_list_fruits[-100])
# IndexError: list index out of range

# 10. Write a FOR LOOP in python that prints each item in the list variable in step 2.  
# The staring number MUST be a negative number. The ending number MUST be postive number
# Looking to get each item printed once in order and then a second time in order
#for i in range(-1, 1):
#    for fruit in dt_list_fruits:
#        print(fruit)


# 11. Write a WHILE LOOP in python that does the same thing as 10. 
#i = 0

#while i < len(dt_list_fruits):
#    print(dt_list_fruits[i])
#    i = i + 1



# 12. For loops.
# Write a FOR LOOP in python that prints each item in list variable in step 2.  
# Hint: type this into google "loop python"
#for i in range(2):
#    for fruit in dt_list_fruits:
#        print(fruit)

# 13. Repeat step 12 but instead of the list variable, use the dictionary variable. 
# Print each key
#for key in dt_dictionary_zoe:
#    print(key)


# 14. Repeat step 13. Instead of printing each key, print each value
# Hint: google "dictionary values python"
#for values in dt_dictionary_zoe.values():
#    print(values)