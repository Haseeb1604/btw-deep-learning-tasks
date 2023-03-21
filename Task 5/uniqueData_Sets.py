import time

# Example 1: Removing duplicates from a list
fruits = ['apple', 'banana', 'cherry', 'apple', 'cherry']

start_time = time.time()

unique_fruits = list(set(fruits))

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Original list: {fruits}")
print(f"Unique fruits: {unique_fruits}")
print(f"Elapsed time: {elapsed_time:.2f} seconds")

# Example 2: Removing duplicates from a string
text = "the quick brown fox jumps over the lazy dog"

start_time = time.time()

unique_chars = set(text)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Original text: {text}")
print(f"Unique characters: {unique_chars}")
print(f"Elapsed time: {elapsed_time:.2f} seconds")


# Output
#   Original list: ['apple', 'banana', 'cherry', 'apple', 'cherry']
#   Unique fruits: ['banana', 'cherry', 'apple']
#   Elapsed time: 0.00 seconds
#   
#   Original text: the quick brown fox jumps over the lazy dog
#   Unique characters: {'r', 'o', 'x', 'j', 'n', 'i', 'b', 'z', 'q', 'e', 't', 'u', 'c', 'k', 'p', ' ', 'a', 's', 'l', 'y', 'd', 'h', 'w', 'f', 'm', 'v', 'g'}
#   Elapsed time: 0.00 seconds
