
ventas = [[0] * 12 for _ in range(3)]

def insertar_venta(ventas, departamento, mes, valor):
    if 0 <= departamento < len(ventas) and 0 <= mes < len(ventas[0]):
        ventas[departamento][mes] = valor
        print(f"Venta Agregada con exito")
    else:
        print("Los índices de departamento o mes no son válidos.")

def buscar_venta(ventas, valor_a_buscar):
    ubicaciones = []
    for departamento in range(len(ventas)):
        for mes in range(len(ventas[departamento])):
            if ventas[departamento][mes] == valor_a_buscar:
                ubicaciones.append((departamento, mes))
    
    if ubicaciones:
        print(f"🔎 Se encontraron ventas de {valor_a_buscar} en las siguientes ubicaciones: {ubicaciones}")
    else:
        print(f"No se encontró ninguna venta con el valor")
    
    return ubicaciones

def eliminar_venta(ventas, departamento, mes):
    if 0 <= departamento < len(ventas) and 0 <= mes < len(ventas[0]):
        ventas[departamento][mes] = 0
        print(f"Venta Eliminada exitosamente")
    else:
        print("Los índices de departamento o mes no son válidos.")

def imprimir_ventas(ventas):
    print("\n--- Estado actual de las ventas ---")
    departamentos = ["Ropa", "Deportes", "Juguetería"]
    for i, fila in enumerate(ventas):
        print(f"{departamentos[i]}: {fila}")
    print("-----------------------------------")

imprimir_ventas(ventas)