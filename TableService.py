from constants import *
from Branch import *
from Table import *

class TableService:
    def __init__(self,name, address):
        self.branch = Branch(name, address)

    def AddTable(self, tablenumber, tabletype=TableType.REGULAR):
        self.branch.Tables[tablenumber] = Table(tablenumber, tabletype)

    def RemoveTable(self, tablenumber):
        del self.branch.Tables[tablenumber]
