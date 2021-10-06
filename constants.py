from enum import Enum

class OrderStatus(Enum):
    RECEIVED, PREPARING, COMPLETED, SERVED, CANCELED = 1, 2, 3, 4, 5

class TableStatus(Enum):
    FREE, RESERVED, OCCUPIED = 1,2,3

class PaymentStatus(Enum):
    UNPAID, PAID, REFUNDED = 1,2,3

class TableType(Enum):
    REGULAR, DELUX, SUPERDELUX = 1,2,3
