from constants import *
class Table:
    def __init__(self, number, type = TableType.REGULAR, status= TableStatus.FREE):
        self.TableStatus = status
        self.TableNumber = number
        self.TableType = type
