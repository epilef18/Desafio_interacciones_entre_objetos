from tienda import Supermercado, Farmacia, Restaurante
from producto import Producto

nombre_tienda = input("Ingrese el nombre de la tienda a crear: ")
costo_delivery = int(input("Ingrese el costo de delivery de la tienda creada: "))

print("Indique el tipo de tienda que desea crear: \n")
opcion_tienda = int(input("1: Supermercado \n2: Farmacia\n3: Restaurant\n"))

while True:
    if opcion_tienda == 1:
        tienda = Supermercado(nombre_tienda, costo_delivery)

    elif opcion_tienda == 2:
        tienda = Farmacia(nombre_tienda, costo_delivery)

    elif opcion_tienda == 3:
        tienda = Restaurant(nombre_tienda, costo_delivery)

    else:
        print("Ingrese una opción válida")
        opcion_tienda = int(input("1: Supermercado \n2: Farmacia\n3:Restaurant"))

opcion_ingresar = int(input("¿Desea ingresar un producto?\n 1: Si\n 2: No\n "))
while opcion_ingresar == 1:
    nombre = input("Ingrese el nombre del producto: \n")
    precio = int(input("Ingrese el precio del producto: \n"))
    stock = input("Ingrese el número de stock del producto")
