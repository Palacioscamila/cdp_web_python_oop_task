from wallet import Wallet
from item_manager import show_items, items_list, pick_items

class User:
    def __init__(self, name):
        self.name = name
        self.wallet = Wallet(self)  # Cada instancia de Usuario tiene una billetera con él mismo como propietario.

    def show_items(self):
        show_items(self)

    def items_list(self):
        return items_list(self)

    def pick_items(self, number, quantity):
        return pick_items(self, number, quantity)
