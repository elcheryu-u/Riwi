# Instrucciones de uso

## Menú

Al iniciarse el programa este va a verificar si se tiene la cantidad mínima de productos (5). Si este no es el caso se le va a pedir que los ingrese. Si los productos iniciales son menos a 5 pero no son 0 solo se le van a pedir los que hagan falta para llegar a 5.

Cuando se cumplan el requisito de los productos se va a mostrar el menú que contiene 6 opciones.

1. Agregar producto/s (`addProducts()`)
2. Consultar producto (`searchProduct()`)
3. Actualizar producto (`updateProduct()`)
4. Eliminar producto (`deleteProduct()`)
5. Calcular valor total del inventario (`calculateInventoryValue()`)
6. Cerrar el programa

### 1. `addProducts` Agregar productos

Se le va a pedir al usuario cuantos productos quiere añadir. Si no se le pide es porque el parámetro `default_amount` está recibiendolo en su lugar.

El bloque de código que añade los productos se ejecuta en dos bucles. Un `for` para la cantidad de productos que se van a añadir y un `While` para repetir la petición del producto si se ingresa un dato erroneo.

Se le pide al usuario el nombre del producto (`name(str`), el precio (`price(float`) y la cantidad (`amount(int`)

**`name(str`**

Con el nombre verificamos si ya existe en la lista.

**`price(float` & `amount(int`**

Verificamos si son números positivos.

Si todo salio bien, se guarda el producto y muestra un mensaje de confirmación.

#### `default_amount`

Este parámetro se utiliza para establecer la cantidad mínima de productos que se van a añadir. Se utiliza para cumplir con el requerimiento de los 5 productos minimos.

### 2. `searchProduct` Consultar producto

Utiliza `findProduct()` para encontrar el producto y le pasa el argumento `show_details` como `True` para mostrarle al usuario el producto.

El producto se le muestra al usuario por medio de `printProduct()`.

### 3. `updateProduct` Actualizar producto

Utiliza `findProduct()` para encontrar el producto a actualizar.

Se utiliza `printProduct()` para mostrarle al usuario el producto que esta actualizando antes de mostrarle el menú con las opciones.

1. Actualizar nombre
2. Actualizar precio
3. Actualizar cantidad
4. Volver

Se utiliza `validateInput()` para que la respuesta del usuario sea un int.

Dependiendo de la opción que escoja el usuario a un diccionario que tiene la clave y el tipo de los datos que se pueden actualizar.

```python
option_types = [
    { 'value': 'name', 'type': str },
    { 'value': 'price', 'type': float },
    { 'value': 'amount', 'type': int },
]
```

> Si el usuario escoje `2` para poder apuntar al precio se le resta `1`. 

```python
option_types[2 - 1] = { 'value': 'price', 'type': float }

# Se almacena en una tupla un mensaje, la clave `type` y la posición `index` del producto.
current_option = ("Ingresa el nuevo valor", option_types[option - 1]['value'], option_types[option - 1]['type'], option -1)
```

Esto se hace asi ya que se le va a pedir al usuario que ingrese el nuevo valor y para esto vamos a usar una linea pero con los diferentes valores.

```python
# current_option[0] = Mensaje para el usuario
# current_option[1] = Clave del dato que se modificara
# current_option[2] = Tipo de dato que se espera
# current_option[3] = Posición del producto en el inventario.

response = validateInput(current_option[0], current_option[2]) if option_types[current_option[3]]['type'] == str else noNegativeNumbers(current_option[0], current_option[2])                      
```

Dentro de response hay dos funciones. `validateInput()` y `noNegativeNumbers()`. Cada una se ejecuta gracias a una condicional. Si el tipo de dato que se va a cambiar es `str` se ejecuta `validateInput()` si no, se va a ejecutar `noNegativeNumbers()`. Esto es asi para que los números tengan la validación de ser solo positivos.

Se crea una copia del producto desde el inventario para modificarlo y reemplazar el antiguo con el nuevo.

```python
product_updated = inventory[update_product['index']]
```

*update_product es el diccionario del producto que encontramos gracias a `findProduct()`

Se le actualiza la clave

```python
product_updated[current_option[1]] = response
```

Por ultimo se reemplaza el producto antiguo con el nuevo.


### 4. `deleteProduct` Eliminar producto

Utiliza `findProduct()` para encontrar el producto a eliminar.

Si el producto existe se le pregunta al usuario de nuevo para confirmar la eliminación.

### 5. `calculateInventoryValue` Calcular el valor total del inventario

```python
total_value = sum(list(map(lambda x: x['price'] * x['amount'], inventory)))
```
En `inventory` la función lambda multiplica el precio por la cantidad.

El `map` hace que este proceso se ejecute por cada producto.

Lo retornado por el `map` se devuelve como una lista gracias a `list`.

`sum` suma los valores de la lista.

### `findProduct()` Busqueda interna

Está función cumple con buscar el producto por nombre y dar una respuesta. Retorna un diccionario con las claves `name` y `exist` como mínimo.

Cuando un producto existe retorna `exist` como `True` y también devuelve la posición (`index`) de este mismo.

Si el parámetro `show_details` es `True` ademas de lo anterior, va a devolver los detalles del producto (precio, cantidad)

#### `msg`

El mensaje que va en el `input` que pide al usuario.

#### `show_details=False`

Maneja si se retorna el producto con los detalles o con información básica para su manejo.

### `continueFn()` Pausa

Función para realizar una pausa y confirmar continuación con `Enter`

### `printProduct()` Mostrar producto

Función a la que se le pasa como argumento el diccionario de un producto `name`, `price` y `amount` y lo imprime de una forma que sea mas legible para el usuario.

#### `product`

Diccionario de un producto que se utiliza para mostrar la información de este mismo.

### `showProductsList()` Lista de productos

Lista el nombre de los productos en el inventario. Se utiliza antes de `findProduct()` para que el usuario tenga una noción de los productos existentes.

### `noNegativeNumbers()` Validación de positivos

Está función utiliza `validateInput()` y su parámetro `extraValidation` para verificar si un número es positivo.

#### `msg`

Mensaje para `validateInput()`

#### `type`

Tipo de número para `validateInput()`

*`int` o `float`*

### `validateInput()` Validación de entradas de usuario

Está función valida si el tipo del dato ingresado por el usuario es correcto. Además permite agregarle una validación extra.

#### `msg`

Mensaje a mostrar al usuario cuando se le pida un dato.

#### `type`

Tipo de dato que se espera de la respuesta del usuario.

#### `extraValidation`

Función que se ejecuta con el valor ingresado por el usuario. Si es `True` se retorna el valor a usar. Si es `False` muestra el error y repite el ciclo.

## Ejemplo de uso

- Se inicia el programa (Ya existen dos productos)
- ***Se necesita un mínimo de 5 productos para iniciar***
- ***Nombre del producto 3***
- "Tamales"
- ***Ingresa un precio***
- "25.6"
- ***Ingresa una cantidad***
- "3"
- ***Se añadio el producto 3: Tamales***

Repetir proceso con:
- Huevos
    - 9.9
    - 12
- Chocolate
    - 15.9
    - 4

- ***El menú principal se muestra***
- ***¿Qué desea hacer?***
- *Seleccionar la opción 3 - Actualizar producto*
- "3"
- ***Lista con todos los productos***
- ***Nombre del producto***
- "papa"
- ***Ficha con información del producto***
- ***¿Qué desea actualizar de "Papa"?***
- *Seleccionar la opción 2 - Actualizar precio*
- "2"
- ***Ingresa el nuevo valor***
- "13"
- ***Ficha con información del producto***
- *Seleccionar la opción 4 - Salir*
- "4"
- ***El menú principal se muestra***
- *Seleccionar la opción 5 - Calcular valor total del inventario*
- "5"
- ***El valor total del inventario es: $385.20***
- ***Presiona Enter para continuar...***
- ***El menú principal se muestra***
- *Seleccionar la opción 6 - Salir*
- "6"
- ***¡Hasta luego!***