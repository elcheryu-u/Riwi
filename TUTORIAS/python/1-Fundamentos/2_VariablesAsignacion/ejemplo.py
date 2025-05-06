# Variables y Asignación

# En este archivo veremos cómo declarar variables y modificarlas
# No resolveremos los ejercicios directamente, solo daremos ejemplos similares.

# Asignación de una variable con un valor de texto
animal = "gato"
print("Mi animal favorito es un", animal)

# Suma de valores usando variables
x = 7
y = 3
resultado = x + y
print("La suma de x e y es:", resultado)

# Modificando una variable paso a paso
puntos = 0
print("Puntos actuales:", puntos)
puntos = puntos + 5  # Se gana una bonificación
print("Puntos tras bonificación:", puntos)

# Verificando el tipo de una variable
peso = 72.5
print("El tipo de la variable 'peso' es:", type(peso))

# Concatenación con conversión de tipos
numero_mascotas = 2
mensaje = "En casa tenemos " + str(numero_mascotas) + " mascotas."
print(mensaje)

# Ejemplo extendido similar al desafío
producto = "laptop"
precio = 1200
marca = "Lenovo"
print("Producto:", producto + ", Marca:", marca + ", Precio: $" + str(precio))