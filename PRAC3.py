# Función recursiva que devuelve el n-ésimo número de Fibonacci
def fibonacci_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)

# Generar serie de los primeros N números
def serie_fibonacci(n):
    return [fibonacci_rec(i) for i in range(n)]

# Ejemplo: primeros 10 números de Fibonacci
n = 40
print(serie_fibonacci(n))

