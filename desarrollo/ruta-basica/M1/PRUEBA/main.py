inventory = [
    {
        'name': "Papa",
        'price': 15.5,
        'amount': 5
    },
    {
        'name': "Chorizo",
        'price': 30.5,
        'amount': 2
    }
]

# Colors to improve readability on the console
class colors:
    reset = '\033[0m'
    bold = '\033[01m'
    
    # colors
    red = '\033[31m'
    green = '\033[32m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    lightcyan = '\033[96m'

# Function to make a pause when a process is finished. 
def continueFn():
    input(f'{colors.purple}Presiona {colors.yellow}Enter{colors.purple} para continuar...{colors.reset}')

# Function to display the list of products before selecting a product
def showProductsList():
    print(f"\n{colors.bold}{colors.blue}Lista de productos{colors.reset}")
    print(", ".join(list(map(lambda x: f"{colors.lightcyan}{x['name']}{colors.reset}", inventory))))

# Function to display a product in a better way.
def printProduct(product=None):
    # product = { 'name': "product", 'price': 2.55, 'amount': 2 }
    
    # print separator for the name of product
    # x = character for use to separate 
    # y = character length
    # z = character length multiplier
    print_separators = lambda x, y, z=1: f"{x}" * (y * z)
    
    if (product):
        name_length = len(product['name'])
        
        product_name = f"""
{colors.bold}{colors.blue}{print_separators("=",name_length,3)}{colors.reset}
{print_separators(" ",name_length)}{product['name']}{print_separators(" ",name_length)}
{colors.bold}{colors.blue}{print_separators("=",name_length,3)}{colors.reset}"""

        print(f"""
{product_name}
{colors.lightblue}Precio: {colors.yellow}${product['price']}{colors.reset}
{colors.lightblue}Cantidad: {colors.yellow}{product['amount']}{colors.reset} 
""")
        
# Function to validate if a number (int, float) is positive
def noNegativeNumbers(msg="Ingresa un valor numerico", type=int):
    return validateInput(
        msg=msg,
        type=type,
        extraValidation=lambda x: not x < 1,
        extraErrorMsg="El valor no puede ser negativo."
    )

# Function to validate the data that the user enters
def validateInput(msg="Ingresa tu dato:", type=str, extraValidation=None, extraErrorMsg="¡Ha ocurrido un error!"):
    while True:
        # The user response. Uses `msg` to display to the user a custom message
        response = input(f"\n{colors.lightcyan}{msg}{colors.reset}\n{colors.yellow}>{colors.reset} ")
        try:
            # This is for validate the response type. Uses `type` and the previous `response`
            value = type(response)
            
            # If we want to validate something else besides the data type. Uses `extraValidation` and `extraErrorMsg`
            if extraValidation and not extraValidation(value):
                print(f"{colors.red}{extraErrorMsg}{colors.reset}")
                continue
            
            return value
        except ValueError:
            print(f"\n{colors.red}Valor inválido. Ingrese un dato de tipo '{type.__name__}'")
            
# Function that search a product with the name
def findProduct(msg, show_details=False):
    search_name = input(f"\n{colors.lightblue}{msg}\n{colors.yellow}>{colors.reset} ")
    
    return_default = {
        'name': search_name,
        'exist': False
    }
    
    for index, product in enumerate(inventory):
        product_exist = product['name'].lower() == search_name.lower()
        
        return_default = { 
            'name': search_name, 
            'index': index,
            'exist': product_exist
        }
        
        if product_exist:
            # `more_details` = False. Return the `name`, `index` and `exist`
            if not show_details:
                return return_default
            
            # `more_details` = True. Return the product object with `exist` and `index`
            product['exist'] = product_exist
            product['index'] = index
            
            # `exist = True`
            return product
            
    # If the product don't exist will return `name` and `exist = False`
    return return_default
            

def addProducts(default_amount=None):   
    # If default_amount don't exist, prompt the user for an amount
    amount_products = default_amount if default_amount else noNegativeNumbers(
        msg="¿Cuantos productos quieres añadir?",
        type=int
    )
               
    # Start with the inventory length if default_amount is set
    for i in range(len(inventory) if default_amount else 0, amount_products):
        while True:
            product_id = i + 1
            name = findProduct(f"{colors.cyan}\nNombre del producto {product_id}{colors.reset}")
            # example: name = { 'name': search_name, 'exist': False }
            
            if not name['exist']:
                price = noNegativeNumbers(
                    msg="Ingresa un precio",
                    type=float
                )
                
                amount = noNegativeNumbers(
                    msg="Ingresa una cantidad",
                    type=int
                )
                
                inventory.append({
                    'name': name['name'],
                    'price': price,
                    'amount': amount
                })
                
                print(f"\n{colors.green}Se añadio el producto {colors.yellow}{product_id}{colors.green}: {colors.yellow}{name['name']}{colors.reset}")
                break
            else:
                print(f"\n{colors.red}Ya existe un producto llamado {colors.yellow}{name['name']}{colors.reset}")
                continueFn()
                continue

# Search for a product and display its details
def searchProduct():
    showProductsList()
    
    response = findProduct("Nombre del producto", True)
    
    if response['exist']:
        printProduct(response)
        continueFn()
    else:
        print(f"\n{colors.red}No se ha encontrado un producto llamado: {colors.yellow}{response['name']}{colors.reset}")
        continueFn()

# Update anything in a product
def updateProduct():
    showProductsList()
    
    update_product = findProduct("Nombre del producto:", True)
    
    if update_product['exist']:
        while True:
            printProduct(update_product)
            # Menu
            print(f"""{colors.yellow}1.{colors.reset} Actualizar nombre
{colors.yellow}2.{colors.reset} Actualizar precio
{colors.yellow}3.{colors.reset} Actualizar cantidad
{colors.yellow}4.{colors.reset} Volver
""")
            
            option = validateInput(
                msg=f"¿Qué desea actualizar de {update_product['name']}?",
                type=int
            )
            
            if option == 4: break
            
            option_types = [
                { 'value': 'name', 'type': str },
                { 'value': 'price', 'type': float },
                { 'value': 'amount', 'type': int },
            ]
            
            # Store the `text`, `type` and `index` for reuse
            current_option = ("Ingresa el nuevo valor", option_types[option - 1]['value'], option_types[option - 1]['type'], option -1)
            
            response = validateInput(current_option[0], current_option[2]) if option_types[current_option[3]]['type'] == str else noNegativeNumbers(current_option[0], current_option[2])
            
            # Copy of a product from inventory
            product_updated = inventory[update_product['index']]
            
            # Update product value
            product_updated[current_option[1]] = response
            
            # Replace the old product in inventory
            inventory[update_product['index']] = product_updated
    
    else:
        print(f'No se encontro el producto {update_product['nombre']}')
        continueFn()
    
# Delete a product
def deleteProduct():
    showProductsList()
    
    delete_product = findProduct("Nombre del producto a eliminar:", True)
    
    if delete_product['exist']:
        confirm_delete = input(f"\n{colors.yellow}¿Estás seguro de que quieres eliminar {colors.red}'{delete_product['name']}'{colors.yellow}? {colors.lightcyan}S/N{colors.yellow}\n> {colors.reset}")
        
        if 's' in confirm_delete.lower():
            inventory.pop(delete_product['index'])
            
            print(f"\n{colors.red}El producto {colors.yellow}{delete_product['name']}{colors.red} se eliminó exitosamente.{colors.reset}")
            continueFn()
    else:
        print(f'{colors.red}El producto no existe.{colors.reset}')
        continueFn()

# Calculate the total value of the inventory
def calculateInventoryValue():
    total_value = sum(list(map(lambda x: x['price'] * x['amount'], inventory)))
    
    print(f"{colors.purple}\nEl valor total del inventario es: {colors.yellow}${total_value:.2f}{colors.reset}")
    continueFn()
    

def main():
    started = False
    
    while True:
        # Check if the app started with at least 5 products or if the inventory has less than 1 product (0)
        if (not started and len(inventory) < 5) or len(inventory) < 1:
            print(f'{colors.bold}{colors.blue}\nSe necesita un mínimo de 5 productos para iniciar.{colors.reset}', end="\n")
            addProducts(5)
            started = True
            
        # Menu
        print(f"""
{colors.yellow}1.{colors.reset} Agregar producto/s
{colors.yellow}2.{colors.reset} Consultar producto
{colors.yellow}3.{colors.reset} Actualizar producto
{colors.yellow}4.{colors.reset} Eliminar producto
{colors.yellow}5.{colors.reset} Calcular valor total del inventario
{colors.yellow}6. Salir{colors.reset}
""")    
        
        option = input(f"{colors.cyan}¿Qué desea hacer?\n{colors.yellow}>{colors.reset} ")
        
        match option:
            case '1':
                addProducts()
            case '2':
                searchProduct()
            case '3':
                updateProduct()
            case '4':
                deleteProduct()
            case '5':
                calculateInventoryValue()
            case '6':
                print(f"{colors.green}¡Hasta luego!{colors.reset}")
                break
            case _:
                print('Ingresa un valor válido.')

main()