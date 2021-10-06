from abc import ABC
from people import *
from Branch import *

class EmployeeManagementService(ABC):
    def __init__(self, branchname, address):
        self.branch = Branch(branchname, address)

    def AddEmployee(self, name, phone, email, id, password, salary):
        pass
    
    def RemoveEmployee(self, id):
        pass

    def UpdateSalary(self, id, salary):
        pass

class ChefManagementService(EmployeeManagementService):
    def __init__(self, branchname, address):
        super().__init__(branchname, address)

    def AddEmployee(self, name, phone, email, id, password, salary):
        account = Account(id, password)
        chef = Chef(name, phone, email, account, salary)
        self.branch.Chefs[id] = chef

    def RemoveEmployee(self, id):
        del self.branch.Chefs[id]

    def UpdateSalary(self, id, newsalary):
        self.branch.Chefs[id].salary = newsalary

class WaiterManagementService(EmployeeManagementService):
    def __init__(self, branchname, address ):
        super().__init__(branchname, address)

    def AddEmployee(self, name, phone, email, id, password, salary):
        account = Account(id, password)
        waiter = Waiter(name, phone, email, account, salary)
        self.branch.Waiters[id] = waiter

    def RemoveEmployee(self, id):
        del self.branch.Waiters[id]

    def UpdateSalary(self, id, newsalary):
        self.branch.Waiters[id].salary = newsalary

class ReceptionistManagementService(EmployeeManagementService):
    def __init__(self, branchname, address ):
        super().__init__(branchname, address)

    def AddEmployee(self, name, phone, email, id, password, salary):
        account = Account(id, password)
        receptionist = Receptionist( name, phone, email, account, salary)
        self.branch.Receptionists[id] = receptionist

    def RemoveEmployee(self, id):
        del self.branch.Receptionists[id]

    def UpdateSalary(self, id, newsalary):
        self.branch.Receptionists[id].salary = newsalary


