def Singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance

@Singleton
class Branch:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.Chefs = {}
        self.Tables = {}
        self.Receptionists = {}
        self.Waiters = {}
        self.Orders = {}
        self.Customers = {}
        self.Payments= {}