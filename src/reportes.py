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