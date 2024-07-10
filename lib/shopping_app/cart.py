from item_manager import show_items  # Importación fuera de la clase

class Cart:
    def __init__(self, owner):
        self.set_owner(owner)  # Llamada a un método que definiremos
        self.items = []

    def set_owner(self, owner):
        self.owner = owner

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = [item.price for item in self.items]
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            print("Saldo insuficiente para realizar la compra.")
            return False
        else:
            self.owner.wallet.balance -= self.total_amount()
            print("Compra realizada con éxito.")
            return True

    def show_items(self):
        show_items(self.owner)  # Llama a show_items del módulo item_manager

