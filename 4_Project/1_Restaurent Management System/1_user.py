# Customer
# Employee
# Admin

#from orders import Order 
from abc import ABC

# abstract class is one kind of template(CANVA) where there is no implementation
# here abc is a module and ABC is a class
# abc means abstract base classes module 
# A module in python is a file that contains python code (variable , functions ,classes or runnable code )


class User(ABC):
     def __init__(self,name,phone,email,address):
        self.name = name
        self.phone = phone
        self.email = email 
        self.address = address


class Employee(User):
     def __init__(self,name,phone,email,address,age,designation,salary):
        super().__init__(name,phone,email,address)
        self.age = age
        self.designation = designation
        self.salary = salary

emp = Employee("Fahim",2323213,"fahim@gmail.com","Dhaka",23,"Chef",234345)
print(emp.name)


class Admin(User):
    def __init__(self,name,phone,email,address)
         super().__init__(name,phone,email,address)
    
    def add_employee(self,restaurent,employee)
         