# 📘 Tema 2 – Variables y Asignación

## 🧠 ¿Qué es una variable?

Una **variable** es un nombre que se usa para guardar un valor. Es como una **caja etiquetada** donde puedes guardar algo, cambiarlo, y usarlo luego.

En Python, las variables se crean simplemente escribiendo su nombre y asignándoles un valor con el signo `=`.

```python
nombre = "Ana"
edad = 25
pi = 3.1416
```

Aquí, `nombre` guarda un texto, `edad` guarda un entero y `pi` un número decimal.

---

## 📝 Reglas para nombrar variables

1. Deben comenzar con una letra o un guion bajo `_` (no con un número).
2. Pueden contener letras, números y guiones bajos (`_`).
3. Son **sensibles a mayúsculas** (`edad` y `Edad` son distintas).
4. No pueden usar palabras reservadas de Python como `if`, `while`, `for`, `class`, etc.

### ✅ Ejemplos válidos:

```python
nombre = "Carlos"
_total = 100
altura1 = 1.70
```

### ❌ Ejemplos inválidos:

```python
1edad = 20      # ❌ empieza con número
nombre completo = "Luis"  # ❌ contiene espacio
if = True       # ❌ palabra reservada
```

---

## 🔄 Reasignación de variables

Puedes cambiar el valor de una variable en cualquier momento:

```python
contador = 10
contador = contador + 1
print(contador)  # Resultado: 11
```

Incluso puedes cambiar el tipo de dato:

```python
dato = 5         # int
print(type(dato))
dato = "cinco"   # str
print(type(dato))
```

---

## 🔍 La función `type()`

Python tiene una función integrada llamada `type()` que nos permite saber el tipo de dato de una variable:

```python
edad = 30
print(type(edad))  # Resultado: <class 'int'>
```

---

## 🧪 Buenas prácticas

* Usa nombres descriptivos: `nombre_usuario` es mejor que `x` o `n`.
* Evita usar letras sueltas como `a`, `b`, `c` a menos que sea temporal.
* Usa **snake\_case**: palabras separadas por guión bajo, como `precio_total`.
* No pongas tildes ni "ñ" en nombres de variables.

---

## ⚠️ Situaciones comunes

### ❌ Usar una variable sin definirla

```python
print(salario)  # Error: variable no definida
```

### ❌ Usar tipos incompatibles

```python
nombre = "Ana"
edad = 20
print(nombre + edad)  # ❌ Error: str + int
```

Solución:

```python
print(nombre + str(edad))  # ✅
```

---

## 📋 Resumen

| Concepto           | Ejemplo                           | Nota                                |
| ------------------ | --------------------------------- | ----------------------------------- |
| Crear variable     | `x = 10`                          | Asigna un valor                     |
| Reasignar variable | `x = x + 1`                       | Puedes cambiar su valor             |
| Saber tipo         | `type(x)`                         | Devuelve el tipo de dato            |
| Nombres válidos    | `total_ventas`, `edad1`, `_valor` | Usa letras, números y guiones bajos |
