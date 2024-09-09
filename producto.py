# clase componente
class Producto:
    def __init__(self, nombre: str, precio: int, stock: int = 0):
        self.__nombre = nombre
        self.__precio = precio
        self.stock = stock
