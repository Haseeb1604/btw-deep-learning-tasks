import time

# Example 1: Union
set1 = {1, 2, 3}
set2 = {2, 3, 4}

start_time = time.time()

set3 = set1.union(set2)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Union: {set3}")
print(f"Elapsed time: {elapsed_time:.2f} seconds")

# Example 2: Intersection

start_time = time.time()

set3 = set1.intersection(set2)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Intersection: {set3}")
print(f"Elapsed time: {elapsed_time:.2f} seconds")

# Example 3: Difference

start_time = time.time()

set3 = set1.difference(set2)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Difference: {set3}")
print(f"Elapsed time: {elapsed_time:.2f} seconds")

# Example 4: Symmetric difference

start_time = time.time()

set3 = set1.symmetric_difference(set2)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Symmetric Difference: {set3}")
print(f"Elapsed time: {elapsed_time:.2f} seconds")


# Outputs
#   Union: {1, 2, 3, 4}
#   Elapsed time: 0.00 seconds
#   
#   Intersection: {2, 3}
#   Elapsed time: 0.00 seconds
# 
#   Difference: {1}
#   Elapsed time: 0.00 seconds
# 
#   Symmetric Difference: {1, 4}
#   Elapsed time: 0.00 seconds
