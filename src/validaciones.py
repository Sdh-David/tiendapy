def leer_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error- Este campo no puede estar vacío.")

def leer_numero(mensaje, tipo=float, permitir_cero=False):
    while True:
        try:
            valor = tipo(input(mensaje))
            if valor < 0 or (not permitir_cero and valor == 0):
                raise ValueError("El valor debe ser mayor a cero.")
            return valor
        except ValueError as e:
            print(f"Error: Entrada inválida. {e if str(e) != 'could not convert string to float' else 'Debe ingresar un número.'}")