from constants import *
from people import *
from OrderService import *
from Branch import *
from Menu import *

class CustomerService(OrderService):
    def __init__(self, OrderID, TableNumber, WaiterID, branchname, address, status = OrderStatus.RECEIVED):
        super().__init__(OrderID, TableNumber, WaiterID, branchname, address, status = OrderStatus.RECEIVED)
        self.menu = Menu()

    def ShowMenu(self):
        self.menu.DispalyMenu()

    def AddOrderItems(self, id):
        item = self.menu.GetMenuItems(id)
        self.branch.Orders[self.OrderID].OrderItems.append(item)
        

    

    