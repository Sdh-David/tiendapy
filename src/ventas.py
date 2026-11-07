from validaciones import leer_texto, leer_numero
from persistencia import registrar_venta_archivo
from datetime import datetime
from tabulate import tabulate

def procesar_venta(inventario):
    carrito = {}
    print("\n NUEVA VENTA ")
    while True:
        codigo = leer_texto("Código del producto (o 'FIN' para terminar): ").upper()
        if codigo == 'FIN': break
        
        if codigo not in inventario:
            print("Aviso: Producto no encontrado.")
            continue
            
        prod = inventario[codigo]
        if prod['stock'] == 0:
            print("Error: Producto agotado.")
            continue
            
        cantidad = leer_numero(f"Cantidad de '{prod['nombre']}' (Stock disponible: {prod['stock']}): ", tipo=int)
        
        if cantidad > prod['stock']:
            print("Error: La cantidad solicitada supera el stock disponible.")
            continue
            
        if codigo in carrito:
            if carrito[codigo] + cantidad > prod['stock']:
                print("Error: La cantidad acumulada en el carrito supera el stock disponible.")
                continue
            carrito[codigo] += cantidad
        else:
            carrito[codigo] = cantidad
            
    if not carrito:
        print("Venta cancelada (carrito vacío).")
        return

    subtotal = sum(inventario[cod]['precio'] * cant for cod, cant in carrito.items())
    
    descuento = 0
    if subtotal >= 100000:
        descuento = subtotal * 0.10
    elif subtotal >= 50000:
        descuento = subtotal * 0.05
        
    total = subtotal - descuento
    
    print("\n VENTA RESUMEN ")
    tabla = [[inventario[c]['nombre'], cant, f"${inventario[c]['precio']*cant}"] for c, cant in carrito.items()]
    print(tabulate(tabla, headers=["Producto", "Cantidad", "Subtotal"], tablefmt="grid"))
    print(f"Subtotal: ${subtotal}")
    print(f"Descuento aplicado: ${descuento}")
    print(f"TOTAL A PAGAR: ${total}")
    
    while True:
        pago = leer_numero("Monto recibido por el cliente: ")
        if pago < total:
            print("Error: El pago es insuficiente. Intente de nuevo.")
        else:
            print(f"Cambio a devolver: ${pago - total}")
            break
            
    for cod, cant in carrito.items():
        inventario[cod]['stock'] -= cant
        
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    detalles = "; ".join([f"{cod}:{cant}" for cod, cant in carrito.items()])
    registro = f"{fecha}|{total}|{detalles}"
    registrar_venta_archivo(registro)
    print("Venta procesada y stock actualizado exitosamente.")