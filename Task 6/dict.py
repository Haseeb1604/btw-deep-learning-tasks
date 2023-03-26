# Dictionary
# Key Value Paired craated using curly braces {}
# : are used to seperate key and values

# Creating an empty dictionary
my_dict = {}

# For Example Fruits along quantity
my_dict = {'apple': 2, 'banana': 3, 'orange': 1}

# Accessing items
print(my_dict['apple']) # Output: 2

# Adding Items to a Dictionary
my_dict['pear'] = 4
print(my_dict) # Output: {'apple': 2, 'banana': 3, 'orange': 1, 'pear': 4}

# Deleting Items to a Dictionary
my_dict = {'apple': 2, 'banana': 3, 'orange': 1, 'pear': 4}
del my_dict['pear']
print(my_dict) # Output : {'apple': 2, 'banana': 3, 'orange': 1}

# Changing Items to a Dictionary
my_dict['banana'] = 5
print(my_dict) # Output : {'apple': 2, 'banana': 5, 'orange': 1}