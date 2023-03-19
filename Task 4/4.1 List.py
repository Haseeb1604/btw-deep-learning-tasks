
# List declaration and initializing 
fruits = ['apple', 'banana', 'orange', 'kiwi']

# Changing Item in List

fruits[1] = 'pear'

print(fruits) # Output: ['apple', 'pear', 'orange', 'kiwi']

# Adding in List
fruits.append('grape')
print(fruits) # Output: ['apple', 'pear', 'orange', 'kiwi', 'grape']

# - Inserting at specific location
fruits.insert(2, 'mango')
print(fruits) # Output: ['apple', 'pear', 'mango', 'orange', 'kiwi', 'grape']

# Removing in List
# - removing by list item name
fruits.remove('kiwi')
print(fruits) # Output: ['apple', 'pear', 'mango', 'orange', 'grape']

#  - removing by index
fruits.pop(1)
print(fruits) # Output: ['apple', 'mango', 'orange', 'grape']

fruit = ['apple', 'banana', 'orange']
last_fruit = fruit.pop()
print(last_fruit) # Output: 'orange'
print(fruit) # Output: ['apple', 'banana']


# Organizing in List
# - sorting list in ascending order
fruits.sort()
print(fruits) # Output: ['apple', 'grape', 'mango', 'orange']

# - sorting list in descending order
fruits.reverse()
print(fruits) # Output: ['orange', 'mango', 'grape', 'apple']


# Indexing in Lists
# - accessing individual items in a list by their index
print(fruits[0]) # Output: 'orange'

# You can also access items from the end of the list using negative indexing, where -1 represents the last item in the list:
print(fruits[-1]) # Output: 'apple'

# Slicing is another way to access a range of items in a list.
print(fruits[1:3]) # Output: ['mango', 'grape']
