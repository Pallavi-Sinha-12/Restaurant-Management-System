from Branch import *
from CookingService import *
from Accounts import *

class ChefService:
    def __init__(self, id, password, branchname, address):
        self.branchname = branchname
        self.address = address
        self.id = id
        self.password = password

    def ShowServices(self):
        print("The tasks that can be performed by you are - ")
        print("To prepare & complete cooking an order - CookingService")

    def ValidatePassword(self):
        validatePassword = ValidateAccount(self.branchname, self.address)
        return validatePassword.ValidatePassword(self.id, self.password, "Chef")

    def CookingService(self):
        if self.ValidatePassword():
            cookingService = CookingService(self.branchname, self.address)
            return cookingService
        return

