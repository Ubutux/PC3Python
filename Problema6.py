"""Una tienda de autopartes necesita un programa para catalogar sus productos, crear la clase
Catálogo y Producto, realizar un objeto dentro de un catálogo productos el cual debe tener un
método para agregar productos y otra para mostrar toda la lista de productos.
Agregar 2 funcionalidades al catálogo (por ejemplo, filtro según año) , asi mismo se puede
agregar más atributos a los productos para que se puedan hacer otras funcionalidades"""

class Producto:
    def __init__(self, nombre, precio, año, marca, categoria):
        self.nombre = nombre
        self.precio = precio
        self.año = año
        self.marca = marca
        self.categoria = categoria

    def __str__(self):
        return f"{self.nombre} - S/.{self.precio} - {self.año} - {self.marca} - {self.categoria}"


class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        return productos_filtrados

if __name__ == "__main__":
    catalogo = Catalogo()

    producto1 = Producto("Llanta", 100, 2023, "Michelin", "Accesorios")
    producto2 = Producto("Filtro de aceite", 15, 2024, "Bosch", "Repuestos")
    producto3 = Producto("Batería", 150, 2022, "Exide", "Repuestos")

    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.agregar_producto(producto3)

    print("Todos los productos en el catálogo:")
    catalogo.mostrar_productos()

    año_a_filtrar = 2023
    print(f"\nProductos en el catálogo del año {año_a_filtrar}:")
    productos_filtrados = catalogo.filtrar_por_año(año_a_filtrar)
    for producto in productos_filtrados:
        print(producto)