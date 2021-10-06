from constants import *
from datetime import datetime

class Order:
    def __init__(self, OrderID, customer, waiter, status = OrderStatus.RECEIVED):
        self.OrderID = OrderID
        self.status = status
        self.waiter = waiter
        self.customer = customer
        self.OrderItems = []
        self.creationtime = datetime.now()
    

