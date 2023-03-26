# Functions in Python are blocks of reusable code

# To define a function in Python, you use the def keyword
# followed by the function name, parentheses, and a colon

# Defining a function
def greet(name):
    print(f"Hello, {name}!")

# Calling a function
greet("Haseeb")
# Output: Hello, Haseeb!

# Functions returns value using the return keyword
# Returning a value from a function
def sum(x, y):
    return x + y

print(sum(3, 4))
# Output: 7

# Docstring
# docstring  is a string literal that appears as the first statement in a module, class, or function definition
# It describes what the code does, what arguments it takes, what it returns, and any other relevant information.
def square(x):
    """
    Returns the square of a number.
    :param x: The number to be squared.
    :return: The square of x.
    """
    return x ** 2

# Docstrings are accessible via the __doc__ attribute of the object they describe. 
print(square.__doc__)
# Output: 
# Returns the square of a number.
#     :param x: The number to be squared.
#     :return: The square of x.


# We can pass arbitrary number of arguments using the *args and **kwargs syntax
# Using *args and **kwargs
def print_args(*args, **kwargs):
    """This function prints the arguments and keyword arguments passed to it."""
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_args(1, 2, 3, a="apple", b="banana")
# Output:
# Positional arguments:
# 1
# 2
# 3
# Keyword arguments:
# a = apple
# b = banana
