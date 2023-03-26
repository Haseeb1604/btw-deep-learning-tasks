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


# ---------------------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def speak(self):
        print(f"{self.name} says hello!")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        
    def get_student_id(self):
        return self.student_id
    
    def speak(self):
        print(f"{self.name} says hi!")


class Teacher(Person):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        
    def get_teacher_id(self):
        return self.teacher_id
    
    def speak(self):
        print(f"{self.name} says good morning!")


person = Person("Alice", 25)
student = Student("Bob", 20, "12345")
teacher = Teacher("Charlie", 35, "67890")

person.speak() # Output: Alice says hello!
student.speak() # Output: Bob says hi!
teacher.speak() # Output: Charlie says good morning!

print(person.get_name()) # Output: Alice
print(student.get_student_id()) # Output: 12345
print(teacher.get_teacher_id()) # Output: 67890

# --------------------------------------------------------------------
class BankAccount:
    num_accounts = 0
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        BankAccount.num_accounts += 1
        
    def deposit(self, amount):
        self.balance += amount
        return f"${amount} deposited. New balance is ${self.balance}."
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"${amount} withdrawn. New balance is ${self.balance}."
        else:
            return f"Insufficient funds. Current balance is ${self.balance}."
        
    def get_balance(self):
        return f"Current balance is ${self.balance}."
    
    def get_owner(self):
        return self.owner
    
    @classmethod
    def get_num_accounts(cls):
        return cls.num_accounts
    

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest of ${interest} added. New balance is ${self.balance}."
    

class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, transaction_fee=0.01):
        super().__init__(owner, balance)
        self.transaction_fee = transaction_fee
        
    def withdraw(self, amount):
        fee = amount * self.transaction_fee
        total_amount = amount + fee
        if self.balance >= total_amount:
            self.balance -= total_amount
            return f"${amount} withdrawn. Transaction fee of ${fee} deducted. New balance is ${self.balance}."
        else:
            return f"Insufficient funds. Current balance is ${self.balance}."

# create a savings account for John with an initial balance of $1000 and interest rate of 2%
john_savings = SavingsAccount("John", 1000, 0.02)

# add interest to John's savings account
john_savings.add_interest() # returns "Interest of $20.0 added. New balance is $1020.0."

# get the balance of John's savings account
john_savings.get_balance() # returns "Current balance is $1020.0."

# create a checking account for Sarah with an initial balance of $500 and transaction fee of 1%
sarah_checking = CheckingAccount("Sarah", 500, 0.01)

# withdraw $50 from Sarah's checking account
sarah_checking.withdraw(50) # returns "$50 withdrawn. Transaction fee of $0.5 deducted. New balance is $449.5."

# get the owner of Sarah's checking account
sarah_checking.get_owner() # returns "Sarah"

# get the number of bank accounts (savings and checking) created
BankAccount.get_num_accounts() # returns 2
