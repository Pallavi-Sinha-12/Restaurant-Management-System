from WelcomeService import *
from Accounts import *
from CheckoutService import *
from Branch import *

class ReceptionistService:
    def __init__(self, id, password, branchname, address):
        self.id = id
        self.password = password
        self.branchname = branchname
        self.address = address

    def ShowServices(self):
        print("The tasks that can be performed by you are - ")
        print("To book and welcome guest -  WelcomeService")
        print("To manage guest exit - CheckoutService")

    def ValidatePassword(self):
        validatePassword = ValidateAccount(self.branchname, self.address)
        return validatePassword.ValidatePassword(self.id, self.password, "Receptionist")
    
    def WelcomeService(self):
        if self.ValidatePassword():
            welcomeService = WelcomeService(self.branchname,self.address)
            return welcomeService
        else:
            return

    def CheckoutService(self):
        if self.ValidatePassword():
            checkoutService = CheckoutService(self.branchname,self.address)
            return checkoutService
        else:
            return

    

    



