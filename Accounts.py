from constants import *
from abc import ABC
from datetime import datetime
from Branch import *

class ValidateAccountChef:
    def __init__(self, branchname, address):
        self.branch = Branch(branchname, address)

    def CheckPassword(self,id, password):
        if self.branch.Chefs[id].account.password == password:
            print("Password is correct. Logged in successfully")
            return True
        else:
            print("Id or password is invalid...Try Again!")
            return False

class ValidateAccountWaiter:
    def __init__(self, branchname, address):
        self.branch = Branch(branchname, address)

    def CheckPassword(self,id, password):
        if self.branch.Waiters[id].account.password == password:
            print("Password is correct. Logged in successfully")
            return True
        else:
            print("Id or password is invalid...Try Again!")
            return False

class ValidateAccountReceptionist:
    def __init__(self, branchname, address):
        self.branch = Branch(branchname, address)

    def CheckPassword(self,id, password):
        if self.branch.Receptionists[id].account.password == password:
            print("Password is correct. Logged in successfully")
            return True
        else:
            print("Id or password is invalid...Try Again!")
            return False

class ValidateAccount:
    def __init__(self, branchname, address):
        self.branchname = branchname
        self.address = address
        self.EmployeeTypes = {'Chef':ValidateAccountChef, 'Waiter': ValidateAccountWaiter, 'Receptionist': ValidateAccountReceptionist}

    def ValidatePassword(self,id, password, EmployeeType):
        PasswordFactory = self.EmployeeTypes[EmployeeType](self.branchname, self.address)
        return PasswordFactory.CheckPassword(id, password)
    

