# write code on the following
# create a class
class Student:
    # the constructor that initializes the attributes of the class
    def __init__(self,name,age,year):
        # instance attributes(constructor body)
        self.name = name
        self.age = age
        self.year = year
    # the method or behaviour of the class 
    def mine(self):
        print("Name:", self.name, " Age:",self.age, " Year:", self.year)
    
# create an object of the class Student
debbie = Student("debbie",21,"year 2")

# call methods:::they are user defined not generally show(),,,
# debbie.mine()


# simple inheritance
# parent class
class Vehicle:
    def Vehicle_info(self,brand):
        print("carName: ",brand)

# Child class
class Car(Vehicle):
    def car_info(self, color):
        print("brandColor: ", color)

# Create object of Car
car = Car()

# access Vehicle's info using car object
car.Vehicle_info("Volvo")
car.car_info("blue")


# multiple inheritance
# parent class 1
class Person:
    def person_info(self, name, age):
        print('Inside Person class')
        print('Name:', name, 'Age:', age)

# Parent class 2
class Company:
    def company_info(self, company_name, location):
        print('Inside Company class')
        print('Name:', company_name, 'location:', location)

# Child class
class Employee(Person, Company):
    def Employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)

# Create object of Employee
emp = Employee()

# access data
emp.person_info('Jessa', 28)
emp.company_info('Google', 'Atlanta')
emp.Employee_info(12000, 'Machine Learning')


# Polymorphism is the ability of an object to take many forms.
# you can have the same method with different actions.
# the len() function acts on the object as per its data type...
# we have method overrride, override built-in function, polymorphism in class methods