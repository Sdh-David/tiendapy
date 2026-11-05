import os

def cargar_inventario():
    inventario = {}
    if not os.path.exists("data/inventario.txt"):
        print("Aviso: Archivo de inventario no encontrado. Se iniciará uno vacío.")
        return inventario
    