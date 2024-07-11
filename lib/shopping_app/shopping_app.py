from customer import Customer
from item import Item
from seller import Seller

# Crear instancia de Seller y añadir artículos
seller = Seller("Tienda DIC")
items = [
    Item("CPU", 40830, seller),
    Item("memoria", 13880, seller),
    Item("tarjeta madre", 28980, seller),
    Item("unidad de fuente de alimentación", 8980, seller),
    Item("PC", 8727, seller),
    Item("Disco duro de 3,5 pulgadas", 10980, seller),
    Item("SSD de 2,5 pulgadas", 13370, seller),
    Item("M.2 SSD", 12980, seller),
    Item("Enfriador de CPU", 13400, seller),
    Item("tablero grafico", 23800, seller)
]

for item in items:
    seller.add_item(item)

print("🤖 Por favor, ingresa tu nombre")
customer_name = input()
customer = Customer(customer_name)

print("🏧 Por favor, ingresa el monto a cargar a tu billetera")
customer.wallet.deposit(int(input()))

print("🛍️ Empieza a comprar")
end_shopping = False
while not end_shopping:
    print("📜 Lista de productos: ")
    seller.show_items()

    print("⛏️ Por favor, ingrese el número de producto")
    number = int(input())

    print("⛏️ Por favor, ingrese la cantidad del producto")
    quantity = int(input())

    items_to_buy = seller.pick_items(number, quantity)
    if items_to_buy:
        for item in items_to_buy:
            customer.cart.add(item)

    print("🛒 Contenido del carrito:")
    customer.cart.show_items()
    print(f"🤑 Total: {customer.cart.total_amount()}")

    print("😭 ¿Quieres terminar de comprar? (yes/no)")
    end_shopping = input() == "yes"

print("💸 ¿Confirmar tu compra? (yes/no)")
if input() == "yes":
    if customer.cart.check_out():
        for item in customer.cart.items:
            item.set_owner(customer)

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈Resultado┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"🛍️ Productos comprados por {customer.name}:")
customer.show_items()
print(f"💰 Saldo restante en la billetera de {customer.name}: {customer.wallet.balance}")

print(f"📦 Estado del inventario de {seller.name}:")
seller.show_items()
print(f"💰 Saldo en la billetera de {seller.name}: {seller.wallet.balance}")

print("🛒 Contenido del carrito:")
customer.cart.show_items()
print(f"🌚 Total del carrito: {customer.cart.total_amount()}")

print("🎉 ¡Fin!")
