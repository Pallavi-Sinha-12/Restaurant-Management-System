from MenuService import *
from constants import *
from EmployeeManagementService import *
from TableService import *

class AdminService:
    def __init__(self):
        self.__password = "Manager@12"

    def ValidatePassword(self, password):
        if self.__password == password:
            print("Password Validated...You are logged in")
            return True
        else:
            print("Password is wrong...Try again")
            return False
    
    def ShowServices(self):
        print("The tasks that can be performed by you are - ")
        print("To Manage Chef Employement - ChefEmploymentService")
        print("To manage Receptionist Employement - ReceptionistEmploymentService")
        print("To manage Waiter Employement - WaiterEmploymentService ")
        print("To manage Menu and its items - MenuService")
        print("To manage Tables - TableService")

    def ChefManagementService(self, password, branchname, address):
        if self.ValidatePassword(password):
            chefManagementService = ChefManagementService(branchname, address)
            return chefManagementService
        return

    def WaiterManagementService(self, password, branchname, address):
        if self.ValidatePassword(password):
            waiterManagementService = WaiterManagementService(branchname, address)
            return waiterManagementService
        return

    def ReceptionistManagementService(self, password, branchname, address):
        if self.ValidatePassword(password):
            receptionistManagementService = ReceptionistManagementService(branchname, address)
            return receptionistManagementService
        return

    def MenuService(self, password):
        if self.ValidatePassword(password):
            menuService = MenuService()
            return menuService
        return

    def TableService(self, password, branchname, address):
        if self.ValidatePassword(password):
            tableService = TableService(branchname, address)
            return tableService
        return

    
    


    







