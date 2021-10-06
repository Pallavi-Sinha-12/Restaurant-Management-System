def Singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance

@Singleton
class Menu:
    def __init__(self):
        self.menuItems = {}

    def GetMenuItems(self, id):
        return self.menuItems[id]

    def DispalyMenu(self):
        print("Followings items are available in our Restaurant...")
        for item in self.menuItems.values():
            print(item.id, item.title, item.price)
            print(item.description)
