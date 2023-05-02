# write code on the following
# create a class
class Student:
    def __init__(self,name,age,year):
        # instance attributes
        self.name = name
        self.age = age
        self.year = year
    # the method or behaviour of the class 
    def mine(self):
        print("Name:", self.name, " Age:",self.age, " Year:", self.year)
    
# create an object of the class Student
debbie = Student("debbie",21,"year 2")

# call methods:::they are user defined not generally show(),,,
debbie.mine()

