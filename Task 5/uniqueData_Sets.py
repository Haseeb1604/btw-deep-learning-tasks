import random
import time

# Generate a list of random numbers with duplicates
random_list = [random.randint(0, 100) for _ in range(10000)]
print(f"Original list: {random_list[:10]}...{random_list[-10:]}")

# Method 1: Conventional way to remove duplicates
start_time = time.time()

unique_list = []
for number in random_list:
    if number not in unique_list:
        unique_list.append(number)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Unique list using conventional method: {unique_list[:10]}...{unique_list[-10:]}")
print(f"Elapsed time using conventional method: {elapsed_time:.2f} seconds")

# Method 2: Using set to remove duplicates
start_time = time.time()

unique_set = set(random_list)
unique_list_set = list(unique_set)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Unique list using set: {unique_list_set[:10]}...{unique_list_set[-10:]}")
print(f"Elapsed time using set: {elapsed_time:.2f} seconds")


# Output
#   Original list: [74, 32, 93, 40, 83, 42, 47, 34, 64, 21]...[53, 1, 39, 43, 47, 27, 76, 14, 4, 21]
#   
#   Unique list using conventional method: [74, 32, 93, 40, 83, 42, 47, 34, 64, 21]...[23, 55, 30, 87, 57, 82, 88, 86, 85, 17]
#   Elapsed time using conventional method: 0.02 seconds
#   
#   Unique list using set: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]...[91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
#   Elapsed time using set: 0.00 seconds


#   Set method is much faster than the conventional method, especially for larger datasets. 
#   This is because sets are optimized for removing duplicates, 
#   whereas the conventional method has to check each number against the new list for duplicates, 
#   which can be slower.
