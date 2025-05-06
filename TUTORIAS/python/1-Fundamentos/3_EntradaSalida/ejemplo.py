# Tema 3: Entrada y salida de datos

# Ejemplo relacionado al ejercicio 1: presentación
# En lugar de pedir el nombre del usuario, aquí usamos un nombre ficticio
def ejemplo_saludo():
    nombre = "Elena"
    print(f"Hola, {nombre}. ¡Bienvenida!")

# Ejemplo relacionado al ejercicio 2: edad futura
# En este caso, usamos una edad predefinida
def ejemplo_edad():
    edad_actual = 30
    edad_futura = edad_actual + 10
    print(f"En 10 años tendrás {edad_futura} años.")

# Ejemplo relacionado al ejercicio 3: suma de números
# Aquí se suman dos números fijos
def ejemplo_suma():
    numero1 = 4
    numero2 = 9
    suma = numero1 + numero2
    print("La suma es:", suma)

# Ejemplo relacionado al ejercicio 4: concatenación de múltiples datos
# Se usan valores ficticios para ilustrar el formato
def ejemplo_datos_usuario():
    nombre = "Laura"
    edad = 22
    pais = "Argentina"
    print(f"Hola, me llamo {nombre}, tengo {edad} años y soy de {pais}.")

# Ejemplo para el desafío adicional: formulario de comida favorita
# Usamos valores de ejemplo para mostrar el formato final
def ejemplo_formulario_comida():
    nombre = "Juan"
    comida = "pizza"
    veces_por_semana = 5
    print(f"Hola {nombre}, comer {comida} {veces_por_semana} veces a la semana suena divertido.")

# Puedes llamar a las funciones para ver los ejemplos en acción
ejemplo_saludo()
ejemplo_edad()
ejemplo_suma()
ejemplo_datos_usuario()
ejemplo_formulario_comida()
