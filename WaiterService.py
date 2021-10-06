from CustomerService import *
from Accounts import *
from BillService import *
from PaymentService import *

class WaiterService:
    def __init__(self, id, password, branchname, address):
        self.id = id
        self.password = password
        self.branchname = branchname
        self.address = address

    def ShowServices(self):
        print("The tasks that can be performed by you are - ")
        print("To take and manage order from customer - CustomerService")
        print("To Calculate & show Bill - BillService")
        print("To Collect Payment - PaymentService")

    def ValidatePassword(self):
        validatePassword = ValidateAccount(self.branchname, self.address)
        return validatePassword.ValidatePassword(self.id, self.password, "Waiter")

    def CustomerService(self, OrderID, TableNumber, WaiterID):
        if self.ValidatePassword():
            customerService = CustomerService(OrderID, TableNumber, WaiterID, self.branchname,self.address)
            return customerService
        else:
            return
    
    def BillService(self, orderID):
        if self.ValidatePassword():
            billService = BillService(orderID, self.branchname,self.address)
            return billService
        else:
            return

    def PaymentService(self, PaymentID, OrderID, amount, TableNumber):
        if self.ValidatePassword():
            paymentService = PaymentService(PaymentID, OrderID, amount, self.branchname,self.address, TableNumber)
            return paymentService
        else:
            return