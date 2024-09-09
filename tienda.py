from producto import Producto

# usar clase compuesta


class Tienda():

    def __init__(self, nombre_tienda: str, costo_delivery: int) -> None:
        self.__nombre_tienda = nombre_tienda
        self.__costo_delivery = costo_delivery
        self.listado_productos = []

    @property  # getter nombre_tienda
    def nombre_tienda(self):
        return self.__nombre_tienda

    @property  # getter costo delivery
    def costo_delivery(self):
        return self.__costo_delivery

    @property  # getter ingresar_producto
    def ingresar_producto(self, producto: Producto):
        self.__listado_productos.append(producto)

    def realizar_venta(nombre: str, cantidad_requerida: int):
        pass

    def listar_productos():
        pass


class Supermercado(Tienda):
    pass


class Farmacia(Tienda):
    pass


class Restaurante(Tienda):
    pass
