from constants import *
from Branch import *
from people import *

class WelcomeService:
    def __init__(self, name, address):
        self.branch = Branch(name, address)

    def ShowFreeTable(self, type):
        f = 0
        for table in self.branch.Tables.values():
            if table.TableStatus == TableStatus.FREE and table.TableType==type:
                print("You can occupy table- ", table.TableNumber)
                f = 1
                break
        if f==0:
            print("Sorry this table type is not free....Try other Types")

    def ReserveTable(self, TableNumber, name, phone, email):
        self.branch.Tables[TableNumber].TableStatus = TableStatus.RESERVED
        self.branch.Customers[TableNumber] = Customer(name, phone, email) 
        print("Table Number " + str(TableNumber) + " is reserved by " + str(name))

    def OccupyTable(self, TableNumber, name, phone, email):
        self.branch.Tables[TableNumber].TableStatus = TableStatus.OCCUPIED
        self.branch.Customers[TableNumber] = Customer(name, phone, email) 
        print("Table Number " + str(TableNumber) + " is occupied by " + str(name))

    

    


