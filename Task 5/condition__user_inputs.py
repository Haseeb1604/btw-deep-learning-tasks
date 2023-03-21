import time

age = input("What's your age? ")
start_time = time.time()

try:
    age = int(age)
except ValueError:
    print("Please enter a valid integer age")
else:
    if age < 0:
        print("Age can't be negative")
    elif age < 18:
        print("You are a minor")
    elif age < 65:
        print("You are an adult")
    else:
        print("You are a senior citizen")

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")

# Input
# What's your age? 25
# 
# Output
# You are an adult
# Elapsed time: 0.00 seconds
# 
# Input
# What's your age? abc
# 
# Output
# Please enter a valid integer age
# Elapsed time: 0.00 seconds

