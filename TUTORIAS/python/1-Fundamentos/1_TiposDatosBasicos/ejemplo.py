# Tipos de datos básicos en Python

# En este ejemplo veremos cómo usar los tipos de datos básicos en Python:
# int, float, str y bool.

# Declaración de variables de distintos tipos
nombre = "Tu Nombre"        # str: una cadena de texto
edad = 25                   # int: un número entero
altura = 1.70               # float: un número con decimales
mayor_edad = True           # bool: valor lógico

# Concatenar información en un mensaje
# NOTA: recuerda convertir los números a texto con str()
mensaje = "Hola, me llamo " + nombre + \
          ", tengo " + str(edad) + \
          " años, mido " + str(altura) + \
          " metros y ¿soy mayor de edad?: " + str(mayor_edad)

print(mensaje)

# Entrada del usuario con input()
# NOTA: input() siempre devuelve un str, así que hay que convertirlo
edad_usuario = int(input("¿Cuántos años tienes? "))
mayor_edad_usuario = edad_usuario >= 18

print("¿Eres mayor de edad?:", mayor_edad_usuario)

# Puedes experimentar con type() para ver el tipo de cada variable
tipo_de_nombre = type(nombre)
print("El tipo de la variable 'nombre' es:", tipo_de_nombre)

# También puedes probar qué valores son considerados True o False
print(bool(0))       # False
print(bool(1))       # True
print(bool(""))      # False
print(bool("Hola"))  # True
