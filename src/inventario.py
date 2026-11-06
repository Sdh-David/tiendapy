from validaciones import leer_texto, leer_numero
from tabulate import tabulate

def agregar_producto(inventario):
    codigo = leer_texto("Código del producto (ej. LAC001): ").upper()
    if codigo in inventario:
        print("Error: El código ya existe en el inventario.")
        return
    
    nombre = leer_texto("Nombre del producto: ")
    categoria = leer_texto("Categoría (Lácteos, Bebidas, Aseo, Abarrotes, Snacks): ")
    precio = leer_numero("Precio de venta: ")
    stock = leer_numero("Stock inicial: ", tipo=int)
    stock_min = leer_numero("Stock mínimo para alertas: ", tipo=int)
    proveedor = leer_texto("Proveedor habitual: ")
    
    inventario[codigo] = {
        "nombre": nombre, "categoria": categoria, "precio": precio,
        "stock": stock, "stock_minimo": stock_min, "proveedor": proveedor
    }
    print(f"Producto '{nombre}' agregado exitosamente.")