from constants import *
from abc import ABC
from datetime import datetime

class Account:
    def __init__(self, id, password=None):
        self.id = id
        self.password = password

class Person(ABC):
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class Customer(Person):
    def __init__(self, name, phone, email):
        super().__init__(name, phone, email)

class Employee(Person):
    def __init__(self, name, phone, email, account):
        super().__init__(name,phone,email)
        self.account = account
    
class Receptionist(Employee):
    def __init__(self, name, phone, email, account, salary):
        super().__init__(name,phone,email, account)
        self.account = account
        self.joiningdate = datetime.today()
        self.salary = salary

class Chef(Employee):
    def __init__(self, name, phone, email, account, salary):
        super().__init__(name,phone,email, account)
        self.account = account
        self.joiningdate = datetime.today()
        self.salary = salary

class Waiter(Employee):
    def __init__(self, name, phone, email, account, salary):
        super().__init__(name,phone,email, account)
        self.account = account
        self.joiningdate = datetime.today()
        self.salary = salary



        
