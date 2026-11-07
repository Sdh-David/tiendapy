from persistencia import cargar_inventario, guardar_inventario
from inventario import agregar_producto, consultar_producto, modificar_producto, eliminar_producto
from ventas import procesar_venta
from reportes import alertas_stock, cierre_del_dia

def main():
    inventario = cargar_inventario()
    
    while True:
        print("\n TIENDA DE DON AURELIO ")
        print("1. Agregar producto")
        print("2. Consultar productos (Listar o Buscar)")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Procesar nueva venta")
        print("6. Ver alertas de stock")
        print("7. Generar cierre del día")
        print("8. Guardar y Salir")
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == '1':
            agregar_producto(inventario)
        elif opcion == '2':
            consultar_producto(inventario)
        elif opcion == '3':
            modificar_producto(inventario)
        elif opcion == '4':
            eliminar_producto(inventario)
        elif opcion == '5':
            procesar_venta(inventario)
        elif opcion == '6':
            alertas_stock(inventario)
        elif opcion == '7':
            cierre_del_dia(inventario)
        elif opcion == '8':
            guardar_inventario(inventario)
            print("Inventario guardado exitosamente. ¡Hasta pronto!")
            break
        else:
            print("Error: Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()