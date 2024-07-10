from item import Item
from tabulate import tabulate
from itertools import groupby

def items_list(user):  # Devuelve todas las instancias de elementos propiedad del usuario.
    items = [item for item in Item.item_all() if item.owner == user]
    return items

def pick_items(user, number, quantity):  # Devuelve la cantidad especificada de instancias de elementos que posee y que corresponden al número.
    items = filter(lambda x: x["number"] == number, _stock(user))
    items = list(items)
    if len(items) == 0 or len(items[0]["items"]) < quantity:
        return []
    else:
        return items[0]["items"][0:quantity]

def show_items(user):  # Muestra el estado del inventario de sus propias instancias de artículos en formato de tabla.
    table_data = []
    for stock in _stock(user):
        table_data.append([stock['number'], stock['label']['name'], stock['label']['price'], len(stock['items'])])
    print(tabulate(table_data, headers=["Número", "Nombre del producto", "Precio", "Cantidad"], tablefmt="grid"))

def _stock(user):  # Devuelve el estado del stock de la instancia del artículo que posee.
    item_ls = items_list(user)
    item_ls.sort(key=lambda m: m.name)
    group_list = [list(group) for _, group in groupby(item_ls, key=lambda m: m.name)]
    stock = []
    for index, item_group in enumerate(group_list):
        stock.append({"number": index, "label": {"name": item_group[0].name, "price": item_group[0].price}, "items": item_group})
    return stock
