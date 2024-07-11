class Item:
    instances = []

    def __init__(self, name, price, owner=None):
        self.name = name
        self.price = price
        self.set_owner(owner)
        Item.instances.append(self)

    def label(self):
        return {"name": self.name, "price": self.price}

    def set_owner(self, owner):
        self.owner = owner

    @staticmethod
    def item_all():
        return Item.instances
