from constants import *
from Branch import *
from Payments import *

class CheckoutService:
    def __init__(self, name, address):
        self.branch = Branch(name, address)
    
    def CheckPayment(self, TableNumber):
        if self.branch.Payments[TableNumber][0]==PaymentStatus.PAID:
            print("You can check out...Thank you")
        else:
            print("Your Payment is unpaid...Please Clear it.")

    def FreeTable(self, TableNumber):
        self.branch.Tables[TableNumber].status = TableStatus.FREE
        print("Freed Table number - ", TableNumber)

    def RecordInfo(self, TableNumber):
        customer = self.branch.Customers[TableNumber]
        amount = self.branch.Payments[TableNumber][1]
        with open('CustomerRecords.txt', 'a') as file:
            text =str(customer.name) +" " + str(customer.email) + " " + str(customer.phone) + " " + str(amount) + "\n"
            file.write(text)

    def ClearCustomerAndPayments(self, TableNumber):
        del self.branch.Customers[TableNumber]
        del self.branch.Payments[TableNumber]
        


