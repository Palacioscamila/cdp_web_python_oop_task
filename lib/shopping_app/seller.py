from user import User
from item_manager import show_items, items_list, pick_items

class Seller(User):
    def __init__(self, name):
        super().__init__(name)
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

    def show_items(self):
        show_items(self)

    def items_list(self):
        return items_list(self)

    def pick_items(self, number, quantity):
        items = pick_items(self, number, quantity)
        if items:
            for item in items:
                self.remove_item(item)
        return items
