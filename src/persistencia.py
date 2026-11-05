import os

def cargar_inventario():
    inventario = {}
    if not os.path.exists("data/inventario.txt"):
        print("Aviso: Archivo de inventario no encontrado. Se iniciará uno vacío.")
        return inventario
    
    with open("data/inventario.txt", "r", encoding="utf-8") as f:
        for linea in f:
            datos = linea.strip().split("|")
            if len(datos) == 6:
                try:
                    codigo, nombre, categoria = datos[0], datos[1], datos[2]
                    precio, stock, stock_min = float(datos[3]), int(datos[4]), int(datos[5])
                    proveedor = "Desconocido"
                except ValueError:
                    continue
            elif len(datos) == 7:
                try:
                    codigo, nombre, categoria = datos[0], datos[1], datos[2]
                    precio, stock, stock_min = float(datos[3]), int(datos[4]), int(datos[5])
                    proveedor = datos[6]
                except ValueError:
                    print(f"Aviso: Línea corrupta omitida -> {linea.strip()}")
                    continue
            else:
                continue
                
            inventario[codigo] = {
                "nombre": nombre, "categoria": categoria, "precio": precio,
                "stock": stock, "stock_minimo": stock_min, "proveedor": proveedor
            }
    return inventario

def guardar_inventario(inventario):
    with open("data/inventario.txt", "w", encoding="utf-8") as f:
        for cod, d in inventario.items():
            f.write(f"{cod}|{d['nombre']}|{d['categoria']}|{d['precio']}|{d['stock']}|{d['stock_minimo']}|{d['proveedor']}\n")

def registrar_venta_archivo(registro):
    with open("data/ventas.txt", "a", encoding="utf-8") as f:
        f.write(registro + "\n")