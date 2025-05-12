# 🧪 Ejercicios – Tema 1: Tipos de datos básicos en Python

*Recuerda realizar los ejercicios por tu propia cuenta, trata de no buscar información por internet ni utilizar IA's. Si necesitas ayuda, en esta misma carpeta se encuentra un archivo [ejemplo.py](./ejemplo.py) para que veas casos de uso.*

En este conjunto de ejercicios, pondrás en práctica los tipos de datos básicos en Python: `int`, `float`, `str` y `bool`. Asegúrate de entender cada tipo antes de resolver los retos.

---

## ✅ Ejercicio 1: Mis datos personales

Crea un programa que declare las siguientes variables y luego imprima un mensaje completo usando concatenación:

- `nombre`: tu nombre (tipo `str`)
- `edad`: tu edad (tipo `int`)
- `altura`: tu altura en metros (tipo `float`)
- `mayor_edad`: un valor `True` o `False` según si eres mayor de edad (tipo `bool`)

📌 **Salida esperada:**

```
Hola, me llamo Ana Gómez, tengo 25 años, mido 1.68 metros y ¿soy mayor de edad?: True
```

---

## ✅ Ejercicio 2: Conversión de tipos

Corrige el siguiente código para que funcione correctamente:

```python
edad = 25
mensaje = "Tienes " + edad + " años"
print(mensaje)
```

📌 **Pista:** No se puede concatenar `str` con `int` sin conversión.

---

## ✅ Ejercicio 3: Detectando el tipo

Crea un script que declare 4 variables (una de cada tipo: `int`, `float`, `str`, `bool`) y use la función `type()` para imprimir su tipo.

📌 **Salida esperada:**

```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

---

## ✅ Ejercicio 4: Entrada del usuario

Pide al usuario su edad usando `input()` y luego determina si es mayor de edad. Imprime el resultado con un mensaje claro.

📌 **Ejemplo de salida:**

```
¿Cuántos años tienes? 17
¿Eres mayor de edad?: False
```

---

## 🧠 Extra: ¿Qué pasa si…?

Experimenta con las siguientes líneas. ¿Qué crees que se imprimirá? ¿Por qué?

```python
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Hola"))
```

Escribe tus respuestas en comentarios y luego verifica ejecutando el código.