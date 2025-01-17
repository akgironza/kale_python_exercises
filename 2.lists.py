

# 1. Write a program that sum of all elements:
one = [613, 955, 291, 497, 562, 483, 165, 210, 864, 789]

print(sum(one))

# 2.  Write a program that find the largest element:
two = [386, 850, 274, 316, 526, 937, 998, 249, 269, 922]
print(max(two))

# 3. Write a program that duplicates that doubles the value of each elements in the list:
# for example: [1,2,3] should result in [2,4,6]
three = [211, 36, 295, 455, 147, 977, 381, 253, 327, 617]

doubled = [num * 2 for num in three]

print(doubled)

# 4. Write a program that concatenates these two list into a single list:
four_a = [582, 427, 534, 143, 567, 604, 12, 48, 686, 825]
four_b = [357, 728, 406, 989, 380, 800, 201, 410, 452, 141]

four_c = four_a + four_b
print(four_c)

# 5. Write a program that removes a specific element from a list by its value.
five = [456, 942, 944, 762, 836, 451, 314, 559, 954, 211]

def fun_5(int):
    if int in five:
        value = five.index(int)
        five.pop(value)
    print(five)

fun_5(456)
        

# 6. Write a program that removes a specific element from a list by its index.
six = [993, 245, 896, 250, 226, 313, 918, 877, 793, 695]

def fun_6(int):
    six.pop(int)
    print(six)

fun_6(1)

# 7. Write a program that sorts a list of numbers in ascending order.
seven = [887, 106, 368, 603, 35, 455, 728, 449, 108, 47]

seven.sort()
print(seven)


# 8. Write a program that filters out all elements in a list that are less than a specified value.
# use for loop and conditionals
eight = [309, 122, 27, 240, 453, 174, 193, 649, 804, 171]
threshold = 200

for i in eight:
    if i < threshold:
        to_pop = eight.index(i)
        eight.pop(to_pop)
print(eight)


# 9. Calculate and print the length (number of elements) of a given list.
nine = [679, 697, 657, 171, 503, 582, 656, 82, 724, 796]

print(len(nine))


# 10. Write a program that take a list and print a subset of its elements by specifying a start and end index.
ten = [64, 800, 662, 185, 630, 612, 181, 210, 738, 12]
start_index = 1
end_index = 4

print(ten[start_index:end_index])


# 11. Write a program iterates the list and
# prints 'FizzBuzz' when divisable by 3 and 5.  
# prints 'Fizz' when divisable by 3 .  
# prints 'Buzz' when divisable by 5. 
eleven = [213, 927, 265, 39, 860, 421, 550, 884, 991, 1500]

for i in eleven:
    if (i % 3 == 0 and i % 5 == 0):
        print('FizzBuzz')
    elif (i % 3 == 0):
        print ('Fizz')
    elif (i % 5 == 0):
        print ('Buzz')
    else:
        print(i)


# 12. Write a program that appends an element to the end of a list.
twelve = [36, 632, 155, 350, 746, 642, 113, 534, 9, 34]

def fun_12(int):
    twelve.append(int)
    print(twelve)

fun_12(122)

# 13. Write a program that inserts an element at a specific position in a list.
thirteen = [191, 871, 990, 163, 687, 747, 606, 799, 373, 851]
element_to_insert = 4

def fun_13(element):
    thirteen.insert(2, element)
    print(thirteen)

fun_13(element_to_insert)
    


# 14. Write a program that counts how many times a specific element appears in a list.
fourteen = [1, 1, 1, 2, 2, 1, 3, 3, 2, 1]
element_to_count = 1

# try using for loop and conditional
i = 0
for num in fourteen:
    if num == element_to_count:
        i = i + 1
    else:
        continue
print(i)

# and then try .count() method
print(fourteen.count(element_to_count))


# 15.  Write a program that extracts all even numbers from a list and stores them in even_only:
# use for loop and conditionals
fifteen = [267, 688, 88, 755, 680, 746, 559, 710, 283, 451]
even_only = []

for i in fifteen:
    if i % 2 == 0:
        even_only.append(i)
    else:
        continue
print(even_only)


# 16. Write a program that reverses this list but does not change the original sixteen variable:
# The answer is not sixteen.reverse(). 
sixteen = [378, 763, 856, 566, 847, 795, 313, 540, 67, 219]

print(list(reversed(sixteen)))


# 17. Write a flattens this double nested listbelow:
# Result should be [1, 2, 3, 4, 5, 6, 7, 8]
# Hint: try a nested loop (2 for in loops) 
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]

flat_list = []

for list in nested_list:
    for num in list:
        flat_list.append(num)
print(flat_list)
        


# 18. Write a program that finds duplicates from the 2 lists below:
# Hint: try a nested loop (2 for in loops) and use equality
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

for num in list1:
    for nums in list2:
        if num == nums:
            print(num)

