import sys

def MemoriaEstatica():
    # Inicialización de un arreglo para almacenar 5 calificaciones.
    calificaciones = [0] * 5
    # Bucle para capturar 5 calificaciones del usuario.
    for i in range(5):
        try:
            # Captura la calificación usando la función input() y la convierte a entero.
            calificaciones[i] = int(input("captura la calificacion: "))
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")
            i -= 1

if __name__ == "__main__":
    MemoriaEstatica()
    
def MemoriaDinamica():

    frutas = [] 
    frutas.append("Mango")
    frutas.append("Manzana")
    frutas.append("Banana")
    frutas.append("Uvas")

    print(frutas)


    frutas.remove("Mango") 
    frutas.remove("Banana") 
    frutas.append("sandia")
    
    print(frutas)

if __name__ == "__main__":
    MemoriaDinamica()