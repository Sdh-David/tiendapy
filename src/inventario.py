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

def listar_productos(inventario, filtro_cat=None):
    if not inventario:
        print("El inventario está vacío.")
        return
    
    tabla = []
    for cod, d in inventario.items():
        if filtro_cat and d['categoria'].lower() != filtro_cat.lower():
            continue
        tabla.append([cod, d['nombre'], d['categoria'], f"${d['precio']}", d['stock'], d['proveedor']])
        
    if not tabla:
        print("No se encontraron productos con esa categoría.")
        return
        
    print(tabulate(tabla, headers=["Código", "Nombre", "Categoría", "Precio", "Stock", "Proveedor"], tablefmt="grid"))

def consultar_producto(inventario):
    print("\n1. Buscar por código")
    print("2. Buscar por categoría")
    opcion = input("Seleccione una opción: ").strip()
    
    if opcion == '1':
        codigo = leer_texto("Ingrese el código del producto: ").upper()
        if codigo in inventario:
            d = inventario[codigo]
            tabla = [[codigo, d['nombre'], d['categoria'], f"${d['precio']}", d['stock'], d['proveedor']]]
            print(tabulate(tabla, headers=["Código", "Nombre", "Categoría", "Precio", "Stock", "Proveedor"], tablefmt="grid"))
        else:
            print("Aviso: El producto no existe.")
    elif opcion == '2':
        categoria = leer_texto("Ingrese la categoría a buscar: ")
        listar_productos(inventario, filtro_cat=categoria)
    else:
        print("Opción inválida.")

def modificar_producto(inventario):
    codigo = leer_texto("Ingrese el código del producto a modificar: ").upper()
    if codigo not in inventario:
        print("Aviso: El producto no existe.")
        return
    
    print("Ingrese 0 si desea mantener el valor actual.")
    nuevo_precio = leer_numero(f"Nuevo precio (actual: ${inventario[codigo]['precio']}): ", permitir_cero=True)
    nuevo_stock = leer_numero(f"Nuevo stock (actual: {inventario[codigo]['stock']}): ", tipo=int, permitir_cero=True)
    
    if nuevo_precio > 0: inventario[codigo]['precio'] = nuevo_precio
    if nuevo_stock > 0: inventario[codigo]['stock'] = nuevo_stock
    print("Producto actualizado.")

def eliminar_producto(inventario):ss
    codigo = leer_texto("Ingrese el código del producto a eliminar: ").upper()
    if codigo not in inventario:
        print("Aviso: El producto no existe.")
        return
    
    del inventario[codigo]
    print("Producto eliminado exitosamente.")