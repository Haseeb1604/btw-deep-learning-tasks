# Inheritance
# Inheritance in classes is a way of creating new classes that inherit the properties and methods of an existing class. 
# The new class, called a subclass, can add new functionality or modify the behavior of the parent class, called the superclass.

# we define an Animal class that has a constructor method that takes a name parameter 
# and initializes an instance variable name. 
# The Animal class also has a speak() method that prints a message to the console.
class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("Animal speaks!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def speak(self):
        print("Meow!")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def speak(self):
        print("Woof!")

# We then define two subclasses of Animal, Cat and Dog, 
# that inherit from the Animal class. 
# The Cat and Dog classes have their own speak() methods 
# that override the parent speak() method with their own implementations.

my_cat = Cat("Whiskers")
my_dog = Dog("Buddy")

my_cat.speak()
my_dog.speak()
# Output:
# Meow!
# Woof!
