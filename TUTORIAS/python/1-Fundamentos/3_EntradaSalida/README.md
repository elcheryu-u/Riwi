# 📘 Tema 3 – Entrada y salida de datos en Python

## 🖨️ La función `print()`

`print()` se utiliza para mostrar información en pantalla. Puedes mostrar texto, números, resultados de operaciones o el valor de variables.

```python
print("Hola mundo")
nombre = "Ana"
print("Hola", nombre)
```

También puedes usar concatenación o f-strings para unir texto:

***f-strings**: Son una forma sencilla y legible de dar formato a cadenas, permitiendo la inclusión de variables y expresiones directamente dentro de la cadena.*

```python
edad = 25
print("Tienes " + str(edad) + " años")
print(f"Tienes {edad} años")  # f-string
```

---

## 🎤 La función `input()`

`input()` sirve para pedir datos al usuario. Siempre devuelve una **cadena de texto** (`str`), aunque parezca un número.

```python
nombre = input("¿Cómo te llamas? ")
print("Hola,", nombre)
```

Para convertir los datos a otros tipos:

```python
edad = int(input("¿Cuántos años tienes? "))
altura = float(input("¿Cuánto mides? "))
```

---

## ⚠️ Conversión de tipos

Recuerda que `input()` devuelve texto, así que si necesitas usar el dato como número, conviértelo:

```python
num1 = input("Ingresa un número: ")
num2 = input("Ingresa otro número: ")
suma = int(num1) + int(num2)
print("La suma es:", suma)
```

---

## 🧪 Buenas prácticas

* Muestra siempre instrucciones claras al usuario.
* Convierte los tipos de datos que necesites usar como números.
* Usa `f-strings` para escribir mensajes más legibles.

---

## ❌ Errores comunes

### Usar el dato sin convertirlo

```python
num = input("Número: ")
print(num + 5)  # ❌ Error: estás sumando texto con número
```

✅ Solución:

```python
num = int(input("Número: "))
print(num + 5)
```

---

## 📋 Resumen

| Acción               | Código                          | Resultado                        |
| -------------------- | ------------------------------- | -------------------------------- |
| Mostrar mensaje      | `print("Hola")`                 | Muestra "Hola" en pantalla       |
| Pedir texto          | `input("¿Nombre?")`             | Guarda lo que escribe el usuario |
| Convertir a número   | `int(input(...))`, `float(...)` | Transforma texto en número       |
| Concatenar valores   | `"Hola " + nombre`              | Une texto con variables          |
| Formato con f-string | `f"Hola {nombre}"`              | Texto dinámico                   |
