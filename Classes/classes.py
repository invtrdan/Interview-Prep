"""
Class
    - blueprint for creating objects
    - Use the PascalNamingConvention
    
Constructor
    - sets initial values
    - executed when a new object is created

self
    - reference to the current object
    
Instance Attribute
    - unique for each instance
    
Class Attributes
    - shared by all instances of a class
    
Object
    - instance of a class
"""


# Creating a Class
class Student:
    school = "Howard University"  # Class Attribute

    # Constructor
    def __init__(self, name):
        self.name = name  # Instance Attribute

    def __str__(self):
        """
        Return string representation of object
        """
        return f"({self.name}, {self.school})"

    # Instance Method
    def print_student_details(self):
        print(f"Name: {self.name}")

    # Class Method
    @classmethod  # Decorator
    def new_student(cls):
        return cls("")

    def __eq__(self, other):
        """
        Magic method to compare 2 objects
        """
        return self.name == other.name


# Object
danielle = Student("Danielle McIntosh")

print(type(danielle))
print(isinstance(danielle, Student))

danielle.print_student_details()

print(Student.school)
print(danielle.school)

new_student = Student.new_student()
print(new_student.school)

print(danielle.__str__())
