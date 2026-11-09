# Define a Employee class with attributes role, department, and salary. 
# This class also has a showDetails() method.
# Create an Engineer class that inherits propertirs from Employee and has additional attributes: name and age


class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("Role:", self.role)
        print("Department:", self.department)
        print("Salary:", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "Development", 75000)

eng1 = Engineer("Alice", 30)
eng1.showDetails()
