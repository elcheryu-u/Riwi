# 📘 Tema 4 – Operadores matemáticos y de comparación

Si estás realizando un tema por día o algo por el estilo, **recomiendo enormemente** realizar este tema ***(Tema 4 – Operadores matemáticos y de comparación)*** y el Tema 5 ***(Condicionales: `if`, `else`, `elif`)*** en conjunto, dado que los operadores son esenciales para definir las condiciones que se evalúan en las estructuras `if`, `else`, `elif`. Trabajarlos juntos facilitará tu comprensión.

## ➕ Operadores matemáticos (aritméticos)

Python permite hacer operaciones básicas como suma, resta, multiplicación y división, así como otras más avanzadas. Estos operadores funcionan tanto con números enteros (`int`) como con decimales (`float`).

### 🔢 Operadores disponibles:

| Operador | Descripción                | Ejemplo  | Resultado |
| -------- | -------------------------- | -------- | --------- |
| `+`      | Suma                       | `3 + 2`  | `5`       |
| `-`      | Resta                      | `5 - 1`  | `4`       |
| `*`      | Multiplicación             | `2 * 3`  | `6`       |
| `/`      | División                   | `10 / 2` | `5.0`     |
| `//`     | División entera (sin dec.) | `9 // 2` | `4`       |
| `%`      | Módulo (residuo)           | `9 % 2`  | `1`       |
| `**`     | Potencia                   | `2 ** 3` | `8`       |

### 🧠 ¿Cuándo usar cada operador?

* Usa `/` cuando quieras un resultado decimal, aunque sean números enteros.
* Usa `//` cuando solo te interese la parte entera del cociente (por ejemplo, dividir objetos entre grupos sin dejar fracciones).
* Usa `%` cuando quieras saber si un número es divisible por otro o cuál es el residuo.
* Usa `**` para hacer potencias en lugar de funciones como `pow()`.

#### ✂ Limitar decimales en divisiones

A veces, al realizar divisiones, el resultado puede tener muchos decimales. Python ofrece varias formas de controlar esto:

1. **Usando `round()`:** Redondea el número a un número específico de decimales. El resultado es un `float`.
    ```python
    resultado = 10 / 3
    resultado_redondeado = round(resultado, 2) # Redondea a 2 decimales
    print(resultado) # Salida: 3.3333333333333335
    print(resultado_redondeado) # Salida: 3.33
    ```
2. **Usando f-strings (formateo de cadenas):** Permite formatear la salida como una cadena con un número específico de decimales.
    ```python
    resultado = 10 / 3
    resultado_formateado = f"{resultado:2.f}" # Formatea a 2 decimales
    print(resultado_formateado)  # Salida: 3.33
    print(type(resultado_formateado)) # El resultado es una cadena (str)
    ```

3. **Usando el método `.format()`:** Otra forma de formatear cadenas.
    ```python
    resultado = 10 / 3
    resultado_formateado = "{:.2f}".format(resultado)
    print(resultado_formateado)  # Salida: 3.33
    ```

4. **Usando el módulo `decimal`:** Para una precisión decimal exacta, especialmente importante en cálculos financieros.

    ```python
    from decimal import Decimal, ROUND_DOWN

    dividendo = Decimal('10')
    divisor = Decimal('3')
    resultado_decimal = dividendo / divisor
    resultado_limitado = resultado_decimal.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
    print(resultado_limitado)  # Salida: 3.33
    print(type(resultado_limitado)) # El resultado es un objeto Decimal
    ```

Elige el método según si necesitas un `float` redondeado para seguir calculando, una cadena formateada para mostrar, o una precisión decimal exacta.

---

## 🔍 Operadores de comparación

Se usan para comparar valores y el resultado es siempre un valor booleano (`True` o `False`). Son muy útiles en condiciones (`if`) y validaciones.

### 🧾 Tabla de operadores:

| Operador | Significado       | Ejemplo    | Resultado |
| -------- | ----------------- | ---------- | --------- |
| `==`     | Igual a           | `5 == 5`   | `True`    |
| `!=`     | Distinto de       | `3 != 4`   | `True`    |
| `>`      | Mayor que         | `7 > 2`    | `True`    |
| `<`      | Menor que         | `2 < 1`    | `False`   |
| `>=`     | Mayor o igual que | `4 >= 4`   | `True`    |
| `<=`     | Menor o igual que | `6 <= 5`   | `False`   |
| `not`    | Negación lógica   | `not True` | `False`   |

### 🧠 ¿Dónde los usamos?

* En estructuras condicionales:

```python
if edad >= 18:
    print("Eres mayor de edad")
```

* Para validar entradas o verificar reglas:

```python
if numero % 2 == 0:
    print("Es un número par")
```

* Para negar una condición:

```python
activo = False
if not activo:
    print("El usuario no está activo")
```

---

## 🔎 Operadores de pertenencia

Los operadores `in` y `not in` permiten comprobar si un elemento existe (o no) dentro de una secuencia como una cadena (`str`), una lista (`list`) u otra colección.

### Ejemplos:

```python
"a" in "manzana"      # True, porque 'a' está en la palabra
"z" not in "manzana"  # True, porque 'z' no aparece en el texto
```

También se pueden usar con listas:

```python
numeros = [1, 2, 3, 4]
print(3 in numeros)      # True
print(5 not in numeros)  # True
```

Se usan mucho para validaciones:

```python
caracter = input("Escribe una letra: ")
if caracter in "aeiou":
    print("Es una vocal")
else:
    print("No es una vocal")
```

---

## 🧪 Combinaciones útiles

Puedes combinar varios operadores en una misma expresión para construir condiciones complejas o cálculos intermedios:

```python
resultado = (5 + 3) * 2   # Resultado: 16
es_valido = (10 % 2 == 0) and (10 > 5)  # True
```

---

## ⚠️ Precauciones comunes

### División entre cero

```python
print(5 / 0)  # ❌ Error: ZeroDivisionError
```

### Tipos incompatibles

```python
print("5" > 3)  # ❌ Error: no se puede comparar texto con número
```

---

## 📋 Resumen rápido

| Acción                 | Código              | Resultado                         |
| ---------------------- | ------------------- | --------------------------------- |
| Suma                   | `x + y`             | Suma de x e y                     |
| Resta                  | `x - y`             | Resta de x e y                    |
| Multiplicación         | `x * y`             | Multiplicación de x e y           |
| División               | `x / y`             | División de x e y                 |
| División entera        | `x // y`            | División de x e y (sin decimales) | 
| Módulo (residuo)       | `x % y`             | Resto de la división              |
| Potencia               | `x ** y`            | x elevado a y                     |
| Comparación igualdad   | `x == y`            | True o False                      |
| Comparación diferencia | `x != y`            | True o False                      |
| Mayor que              | `x > y`             | True o False                      |
| Menor que              | `x < y`             | True o False                      |
| Mayor o igual que      | `x >= y`            | True o False                      |
| Menor o igual que      | `x <= y`            | True o False                      |
| Negación lógica        | `not True`          | False                             |
| Pertenece a            | `'a' in "casa"`     | True                              |
| No pertenece a         | `'z' not in "casa"` | True                              |
