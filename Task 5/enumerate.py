# Using the enumerate() function

# In its simplest form, 
# enumerate() can be used to loop through a sequence while keeping track of the index of each item

fruits = ['apple', 'banana','cherry', 'date']

for index, fruit in enumerate(fruits):
    print(index, fruit)
    
# Output
#   0 apple
#   1 banana
#   2 cherry
#   3 date

# Starting the index at a different number
# We can specify a different starting value by passing it as the second argument to enumerate():

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# Output
#   1 apple
#   2 banana
#   3 cherry
#   4 date

# creating dictionary using enumerate() 
# where the keys are the indices and the values are the items in the sequence:
    
fruit_dict = {index: fruit for index, fruit in enumerate(fruits)}
print(fruit_dict)

# Output
# {0: 'apple', 1: 'banana', 2: 'cherry', 3: 'date'}

import time


start_time = time.time()

for i, fruit in enumerate(fruits):
    time.sleep(0.5)  # Simulate some work
    print(f"Index: {i}, Fruit: {fruit}")

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.2f} seconds")

# Output
#   Index: 0, Fruit: apple
#   Index: 1, Fruit: banana
#   Index: 2, Fruit: cherry
#   Index: 3, Fruit: date
#   Elapsed time: 2.01 seconds

# elapsed time is slightly longer than the sum of the sleep times, due to the overhead of the enumerate() function and the print statements.
