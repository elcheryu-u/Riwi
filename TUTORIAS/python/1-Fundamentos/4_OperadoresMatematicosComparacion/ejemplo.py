# ejemplo.py – Tema 4: Operadores matemáticos y de comparación

# Este archivo contiene ejemplos de uso para diferentes tipos de operadores en Python.
# No resuelve los ejercicios directamente, solo da una idea de cómo se usan estos operadores.

# Operaciones matemáticas básicas
x = 10
y = 3
print("Suma:", x + y)
print("Resta:", x - y)
print("Multiplicación:", x * y)
print("División:", x / y)
print("División entera:", x // y)
print("Residuo:", x % y)
print("Potencia:", x ** y)

# Comparaciones simples
print("¿x es igual a y?", x == y)
print("¿x es mayor que y?", x > y)
print("¿x es menor o igual a y?", x <= y)

# Comparaciones con variables de texto
letra = 'p'
print("¿'p' está en 'python'?", letra in "python")
print("¿'z' no está en 'python'?", 'z' not in "python")

# Uso del operador not
activo = False
print("¿No está activo?", not activo)

# Combinando operadores
numero = 12
es_divisible = (numero % 2 == 0) and (numero % 3 == 0)
print("¿Es divisible por 2 y por 3?", es_divisible)
