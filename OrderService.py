from constants import *
from Order import *
from Branch import * 

class OrderService:
    def __init__(self, OrderID, TableNumber, WaiterID, branchname, address, status = OrderStatus.RECEIVED):
        self.branch = Branch(branchname, address)
        self.OrderID = OrderID
        order = Order(OrderID, self.branch.Customers[TableNumber], self.branch.Waiters[WaiterID], status)
        self.branch.Orders[self.OrderID] = order

    def RecieveOrder(self, status = OrderStatus.RECEIVED):
        self.branch.Orders[self.OrderID].OrderStatus = status
        print("Order is received..order number - ", self.OrderID)

    def GetOrderStatus(self):
        status =  (self.branch.Orders[self.OrderID]).status
        if status==OrderStatus.PREPARING:
            print("Order is being prepared..Wait")
        elif status==OrderStatus.RECEIVED:
            print("Order is received but not strated cooking...")
        return status

    def ServeOrder(self):
        if self.GetOrderStatus()==OrderStatus.COMPLETED:
            self.branch.Orders[self.OrderID].OrderStatus = OrderStatus.SERVED
            print("Food is served...")
        else:
            print("Food is being prepared...Wait for some time")

    def CancelOrder(self):
        self.branch.Orders[self.OrderID].OrderStatus = OrderStatus.CANCELLED

    def ClearOrder(self):
        del self.branch.Orders[self.OrderID]






    