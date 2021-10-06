from constants import *
from Payments import *
from Branch import *

class PaymentService(Payment):
    def __init__(self, PaymentID, OrderID, amount, name, address, TableNumber, status = PaymentStatus.UNPAID):
        super().__init__(PaymentID, OrderID,amount, status = PaymentStatus.UNPAID)
        self.branch = Branch(name, address)

    def ReceivePayment(self):
        self.PaymentStatus = PaymentStatus.PAID
        print("Payment is received....Thank you!")

    def Refund(self):
        self.PaymentStaus = PaymentStatus.REFUNDED

    def GetBillAmount(self):
        print("Payment to be made ",self.amount)
    
    def UpdatePayment(self, TableNumber):
        customer = self.branch.Customers[TableNumber]
        self.branch.Payments[TableNumber] = (PaymentStatus.PAID, self.Amount)

