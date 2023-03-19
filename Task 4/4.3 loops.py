# Looping Over Lists:
#  iterating over the items in a list. 

fruits = ['apple', 'banana', 'orange', 'kiwi']

for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# orange
# kiwi

#  Using range() function to loop over a list 
fruits = ['apple', 'banana', 'orange', 'kiwi']

for i in range(len(fruits)):
    print(fruits[i])

# Output:
#     apple
#     banana
#     orange
#     kiwi


# Looping Over Tuple

# We can loop over a tuple using a for loop
my_tuple = ("apple", "banana", "cherry")
for item in my_tuple:
    print(item)
    
# Avoiding Indentation Errors
my_list = ["apple", "banana", "cherry"]
try:
    for item in my_list:
        print(item)
except IndentationError:
    print("Error: Check your indentation!")


# List vs Tuple

# list is mutable (can be changed) while tuple is immutable (cannot be changed once created).
# Syntax: Lists are created using square brackets [], while tuples are created using parentheses ().
# Performance: Lists are slower than tuples when it comes to indexing and iteration, as lists need to allocate memory each time a new element is added, while tuples allocate all the memory they need when they are created.
# Purpose: Lists are used to store a collection of homogeneous or heterogeneous items, while tuples are used to store a collection of heterogeneous items that belong together, such as a person's name, age, and gender.
# Usage: Lists are commonly used for data manipulation and storage, while tuples are commonly used for passing data around a program, as they are more memory efficient and cannot be changed accidentally.

# List example
my_list = ["apple", "banana", "cherry"]
my_list[1] = "orange"
print(my_list)  # Output: ["apple", "orange", "cherry"]

# Tuple example
my_tuple = ("apple", "banana", "cherry")
# my_tuple[1] = "orange"  # This will give an error, as tuples are immutable
print(my_tuple)  # Output: ("apple", "banana", "cherry")