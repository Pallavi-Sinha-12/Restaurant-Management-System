from Branch import *

class BillService:
    def __init__(self,OrderID, branchname, address):
        self.branch = Branch(branchname, address)
        self.order = self.branch.Orders[OrderID]
        self.__GST = 0.18
    
    def CalculateBill(self):
        bill = 0
        for item in self.order.OrderItems:
            bill = bill + item.price
        bill = bill*self.__GST + bill
        return bill

    def ShowBill(self):
        for item in self.order.OrderItems:
            print( item.title, item.price)
        print("Total Bill including 18 percent GST is ", self.CalculateBill())    