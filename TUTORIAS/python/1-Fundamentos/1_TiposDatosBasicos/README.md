# 📘 Tema 1 – Introducción a Python: Tipos de datos básicos

## 🧠 ¿Qué es un tipo de dato?

Un tipo de dato representa el tipo de valor que una variable puede tener. Python, como lenguaje de programación, necesita saber si una variable es un número, un texto, una lista, etc., para saber qué operaciones puede hacer con ella.

En este primer día, veremos los tipos más básicos: `int`, `float`, `str` y `bool`.

### 🔢 `int` – Números enteros

Un `ìnt` (de "interger") es un número **entero**, es decir, sin decimales. Por ejemplo:

```python
edad = 20
```

Aquí la variable `edad` tiene el valor `20`, que es un número entero.

##### 👉 ¿Qué se puede hacer con un `int`?
- Sumar, restar, multiplicar, dividir.
- Comparar: `==`, `<`, `>`, etc.
- Convertirlo a otros tipos: por ejemplo, a `str` (texto) con `str(edad)`.

##### ⚠️ Situaciones comunes:
- Si haces una división con enteros, el resultado será un `float`:

```python
resultado = 5 / 2 # Resultado: 2.5 (float)
```

- Para divisiones enteras (sin decimales), se usa `//`:

```python
resultado = 5 // 2 # Resultado: 2 (int)
```

---

### 💧 float – Números decimales

Un `float` es un número **con decimales** (punto flotante). Ejemplos:

```python
pi = 3.14
altura = 1.75
```

##### 👉 ¿Qué se puede hacer con un `float`?

Todo lo que puedes hacer con `int`, pero tambien trabajar con valores fraccionarios.

##### ⚠️ Cuidado con la precisión:

A veces, los `float` no son exactos debido a cómo se representan en la memoria del computador:

```python
print(0.1 + 0,2) # Resultado 0.30000000000000004
```

Este es un comportamiento normal en todos los lenguajes de programación, no solo en Python.

---

### 📝 str – Cadenas de texto

Un `str` (de "string") es un texto, una **cadena de caracteres**. Ejemplo:

```python
nombre = "Sergio"
```

Los textos siempre van entre **comillas simples o dobles**:

```python
fruta = 'manzana'
```

##### 👉 ¿Qué se puede hacer con un `string`?

- Concatenar (unir) textos:

```python
saludo = "Hola " + nombre
```

- Acceder a letras individuales (como si fuera una lista):

```python
letra = nombre[0] # Resultado: 'S'
```

- Convertir otros tipos a texto:

```python
texto = str(25) # Resultado: '25'
```

##### ⚠️ Errores comunes:
- Intentar sumar un texto con un número sin convertir:

```python
edad = 25
print("Tienes " + edad + " años") # ❌ Error
```

Solución:

```python
print("Tienes " + str(edad) + " años") # ✅
```

---

### ✅ bool – Valores lógicos (True/False)

Un `bool` representa un valor **verdadero o falso**.

```python
es_mayor = True
es_menor = False
```

##### 👉 ¿Para qué sirve?

Los `bool` se usan para tomar decisiones en el código (por ejemplo, en condicionales):

```python
if es_mayor:
    print("Puedes entrar")
```

##### ⚠️ Importante

Los valores numéricos también pueden convertirse a booleanos:

- `bool(0)` → `False`
- `bool(1)` → `True`
- `bool(-5)` → `True`

Y en el caso de cadenas:

- `bool("")` (cadena vacía) → False
- `bool("Hola")` → True

## Resumén

| Tipo    | Ejemplo          | Significado                     |
| ------- | ---------------- | ------------------------------- |
| `int`   | `10`             | Número entero                   |
| `float` | `3.14`           | Número con decimales            |
| `str`   | `"Hola"`         | Cadena de texto                 |
| `bool`  | `True` / `False` | Valor lógico: verdadero o falso |