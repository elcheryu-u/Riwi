inventario = {
    'test': (5.0, 1),
    'testt': (10.0, 1)
}

# Colores para mejorar legibilidad en la consola
class colors:
    reset = '\033[0m'
    bold = '\033[01m'
    
    # colores
    red = '\033[31m'
    green = '\033[32m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    lightcyan = '\033[96m'

# Función para verificar la validez del dato enviado
# msg: Mensaje a mostrar al momento de pedir el dato
# type: El tipo de dato que se espera recibir
# extraValidation: Validación extra por si se necesita verificar algo mas del dato. Por ejemplo, verificar si dato > 5.
# extraErrorMsg: Mensaje de error a mostrar por si `extraValidation` devuelve error (False)
def requestValidData(msg, type=str, extraValidation=None, extraErrorMsg="Valor no válido."):
    """Solicita y valida datos ingresados por el usuario."""
    while True:
        response = input(f"{colors.blue}{msg}{colors.reset}").strip()
        try:
            value = type(response)
            if extraValidation and not extraValidation(value):
                print(f"{colors.red}{extraErrorMsg}{colors.reset}")
                continue
            return value
        except ValueError:
            print(f"{colors.red}Entrada inválida. Ingresa un valor del tipo {type.__name__}.{colors.reset}")

def productAlreadyExist(name):
    """Verifica si un producto ya existe en el inventario."""
    normalizeName = name.lower()
    return normalizeName in (n.lower() for n in inventario)


# Función para buscar un producto. Para realizar la busqueda se utiliza el nombre del producto.
def searchProduct(name, silent=False):
    """Busca un producto por nombre y muestra su información."""
    normalizeName = name.lower()

    for key in inventario:
        if key.lower() == normalizeName:
            if not silent:
                price, amount = inventario[key]
                print(f"{colors.lightcyan}{name}{colors.reset} -> Precio: {colors.yellow}${price:.2f}{colors.reset} | Cantidad: {colors.yellow}{amount}{colors.reset}")
            return key
    if not silent:
        print(f"{colors.red}Producto no encontrado.{colors.reset}")

        # Buscar sugerencias similares
        suggestions = [key for key in inventario if normalizeName in key.lower()]
        if suggestions:
            print(f"{colors.yellow}¿Quizás quisiste decir alguno de estos productos?:{colors.reset}")
            for s in suggestions:
                print(f" - {colors.cyan}{s}{colors.reset}")
        else:
            print(f"{colors.red}No se encontraron productos similares a '{name}'.{colors.reset}")

    return None

# Funcion para añadir un producto. Se usa el nombre como clave y una tupla (price, amount) como valor.
def addProduct():
    """Flujo para agregar un nuevo producto al inventario."""
    name = requestValidData(
        msg="Nombre del producto: ",
        type=str,
        extraValidation=lambda n: not productAlreadyExist(n),
        extraErrorMsg="El producto ya existe. Ingresa uno nuevo."
    )
    
    price = requestValidData(
        msg="Precio del producto: $",
        type=float
    )
    
    amount = requestValidData(
        msg="Cantidad disponible: ",
        type=int
    )

    inventario[name] = (price, amount)
    print(f"{colors.green}Producto '{name}' añadido correctamente.{colors.reset}")
    returnToMenu(addProduct)

def seeProduct():
    """Flujo para consultar un producto existente."""
    name = requestValidData(
        msg="Nombre del producto a consultar: "
    )

    searchProduct(name)
    returnToMenu(seeProduct)

# Función para actualizar el precio.
def updatePrice():
    """Flujo para actualizar el precio de un producto."""
    name = requestValidData(
        msg="Producto al que deseas actualizar el precio: "
    )

    actualName = searchProduct(name)

    if actualName:
        newPrice = requestValidData(
            msg=f"Nuevo precio para '{actualName}': $",
            type=float
        )

        _, amount = inventario[actualName]
        inventario[actualName] = (newPrice, amount)
        print(f"{colors.green}Precio de '{actualName}' actualizado a ${newPrice:.2f}{colors.reset}")
    else:
        print(f"{colors.red}No se pudo actualizar el precio porque el producto no fue encontrado.{colors.reset}")
    
    returnToMenu(updatePrice)

# Función para borrar el precio.
def deleteProduct():
    """Flujo para eliminar un producto del inventario."""
    
    name = requestValidData(
        msg="Producto a eliminar: "
    )

    actualName = searchProduct(name)

    if actualName:
        confirm = input(f"{colors.yellow}¿Estás seguro de que deseas eliminar '{actualName}'? (S/N): {colors.reset}").strip().lower()
        if confirm == 's':
            del inventario[actualName]
            print(f"{colors.green}Producto '{actualName}' eliminado del inventario.{colors.reset}")
        else:
            print(f"{colors.cyan}Eliminación cancelada.{colors.reset}")
    else:
        print(f"{colors.red}No se pudo eliminar porque el producto no fue encontrado.{colors.reset}")
    
    returnToMenu(deleteProduct)

# Función para calcular el valor total.
def calculateTotalValue():
    """Calcula y muestra el valor total del inventario."""
    total = sum(map(lambda x: x[0] * x[1], inventario.values()))
    print(f"{colors.purple}Valor total del inventario: ${total:.2f}{colors.reset}")
    returnToMenu(calculateTotalValue)

def returnToMenu(actualFunction):
    """Presenta un menú de opciones después de completar una operación."""
    
    print(f"\n{colors.bold}{colors.purple}¿Qué deseas hacer ahora?{colors.purple}")
    print(f"{colors.yellow}1.{colors.reset} Repetir esta operación")
    print(f"{colors.yellow}2.{colors.reset} Volver al menú principal")
    
    while True:
        opcion = input(f"\n{colors.lightblue}Selecciona una opción (1-2):{colors.reset}\n> ").lower()
        print('')
        
        if opcion == '1':
            actualFunction()
            return
        elif opcion == '2':
            return
        else:
            print(f"{colors.red}Opción inválida. Por favor, elige 1 o 2.{colors.reset}")


def mostrar_menu():
    print(f"""
{colors.bold}{colors.cyan}MENÚ DE INVENTARIO{colors.reset}

{colors.yellow}1.{colors.reset} Añadir producto
{colors.yellow}2.{colors.reset} Consultar producto
{colors.yellow}3.{colors.reset} Actualizar precio
{colors.yellow}4.{colors.reset} Eliminar producto
{colors.yellow}5.{colors.reset} Calcular valor total
{colors.yellow}6.{colors.reset} Salir
""")

def main():
    while True:
        print(f"{colors.purple} {inventario} {colors.reset}")
        mostrar_menu()
        opcion = input(f"{colors.lightblue}Elige una opción (1-6): \n> {colors.reset}").strip()

        match opcion:
            case '1':
                addProduct()
            case '2':
                seeProduct()

            case '3':
                updatePrice()

            case '4':
                deleteProduct()

            case '5':
                calculateTotalValue()

            case '6':
                print(f"{colors.green}¡Hasta luego!{colors.reset}")
                break

            case _:
                print(f"{colors.red}Opción inválida. Intenta de nuevo.{colors.reset}")

if __name__ == "__main__":
    main()
