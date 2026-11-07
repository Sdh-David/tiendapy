import os
from tabulate import tabulate

def alertas_stock(inventario):
    alertas = {}
    for cod, d in inventario.items():
        if d['stock'] <= d['stock_minimo']:
            prov = d['proveedor']
            if prov not in alertas:
                alertas[prov] = []
            estado = "AGOTADO" if d['stock'] == 0 else "Bajo stock"
            alertas[prov].append([cod, d['nombre'], d['stock'], estado])
            
    if not alertas:
        print("No hay alertas de stock.")
        return
        
    for prov, items in alertas.items():
        print(f"\nProveedor: {prov}")
        print(tabulate(items, headers=["Código", "Producto", "Stock", "Estado"], tablefmt="simple"))

def cierre_del_dia(inventario):
    if not os.path.exists("data/ventas.txt"):
        print("No hay ventas registradas para generar el cierre.")
        return
        
    total_vendido = 0.0
    num_ventas = 0
    ventas_productos = {cod: 0 for cod in inventario.keys()}
    with open("data/ventas.txt", "r", encoding="utf-8") as f:
        for linea in f:
            if not linea.strip(): continue
            datos = linea.strip().split("|")
            if len(datos) != 3: continue
            
            total_vendido += float(datos[1])
            num_ventas += 1
            
            detalles = datos[2].split(";")
            for detalle in detalles:
                if ":" in detalle:
                    cod, cant = detalle.split(":")
                    cod = cod.strip()
                    cant = int(cant.strip())
                    if cod in ventas_productos:
                        ventas_productos[cod] += cant
                    else:
                        ventas_productos[cod] = cant

    if num_ventas == 0:
        print("No hay ventas válidas para generar el cierre.")
        return

    ticket_promedio = total_vendido / num_ventas
    
    prod_mas_vendido = None
    max_cant = -1
    sin_ventas = []
    
    for cod, cant in ventas_productos.items():
        if cant > max_cant:
            max_cant = cant
            prod_mas_vendido = cod
        if cant == 0 and cod in inventario:
            sin_ventas.append(inventario[cod]['nombre'])
            
    nombre_mas_vendido = inventario[prod_mas_vendido]['nombre'] if prod_mas_vendido in inventario else prod_mas_vendido
    
    print("\n VENTA DEL DIA")
    print(f"Total vendido: ${total_vendido}")
    print(f"Número de ventas: {num_ventas}")
    print(f"Ticket promedio: ${ticket_promedio:.2f}")
    print(f"Producto más vendido: {nombre_mas_vendido} ({max_cant} unidades)")
    
    if sin_ventas:
        print("\nProductos sin ventas hoy:")
        for p in sin_ventas:
            print(f"- {p}")