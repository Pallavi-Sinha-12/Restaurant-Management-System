from constants import *
from Branch import *

class CookingService:
    def __init__(self, name, address):
        self.branch = Branch(name, address)
    
    def GetPendingOrdersList(self):
        print("All pending orders are - ")
        for order in self.branch.Orders.values():
            if order.status == OrderStatus.RECEIVED:
                print(order.OrderID, end = " ")
                for item in order.OrderItems:
                    print(item.title, end = " ")
                print()
    
    def CookOrder(self, Orderid):
        self.branch.Orders[Orderid].status = OrderStatus.PREPARING
        print("Preparing food....with order number ", Orderid)

    def CompleteOrder(self, orderid):
        self.branch.Orders[orderid].status = OrderStatus.COMPLETED
        print("Food is prepared completely....Waiter can serve. The order number is ", orderid)

        

