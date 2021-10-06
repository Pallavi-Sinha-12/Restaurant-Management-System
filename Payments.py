from constants import *

class Payment:
    def __init__(self, PaymentID, OrderID, amount, status = PaymentStatus.UNPAID):
        self.PaymentID =id
        self.PaymentStatus = status
        self.OrderID = OrderID
        self.Amount = amount
        

