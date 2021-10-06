from Menu import *
from MenuItem import *

class MenuService:
    def __init__(self):
        self.menu = Menu()

    def AddMenuItems(self, id, title, description, price):
        menuItem = MenuItem(id, title, description, price)
        self.menu.menuItems[id] = menuItem

    def RemoveMenuItems(self, id):
        del self.menu.menuItems[id]

    def UpdatePrice(self, id, price):
        self.menu.menuItems[id] = price

    def ShowMenu(self):
        self.menu.DispalyMenu()
