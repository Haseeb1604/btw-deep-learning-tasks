# Classes in Python are a way of organizing and encapsulating data and behavior into reusable and extensible objects
# A class defines a blueprint for creating objects that share a common structure and behavior

class Dog:
    # __init__ is a constructor method that will executes whenever the object of that class has been created 
    # self keyword is used to refer to the instance of the Dog class that the method is being called on
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    # The Dog class also has a method bark() that prints a message to the console
    def bark(self):
        print(f"{self.name} barks!")

# To create an instance/Object of the Dog class, 
# we can call the class constructor with the required arguments:
my_dog = Dog("Buddy", "Golden Retriever")

# We can then call the bark() method on the my_dog instance to make it bark:
my_dog.bark()
# Output: Buddy barks!
