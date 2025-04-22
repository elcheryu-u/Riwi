name = None
price = None
amount = None
discount = None
discountRange = range(101)

def getName():
    global name
    nameInput = input("Ingresa el nombre del producto:")
    if nameInput.isdigit():
        print('Error, el nombre no puede ser un número.')
        getName()
    else:
        name = nameInput
        print('gucci: ' + name)

getName()

def getPrice():
    global price
    while True:
        priceInput = input("Ingresa el valor del producto:")
    
        try:
            price = int(priceInput)
            print('guccci')
            break
        except ValueError:
            try:
                price = float(priceInput)
                print('gucci')
                break
            except ValueError:
                print('Error, el precio no puede ser un texto.')
                getPrice()
    
getPrice()

def getAmount():
    global amount
    amountInput = input("Ingresa la cantidad del producto:")
    
    try:
        amount = int(amountInput)
        print('gucci')
    except ValueError:
        print('No se puede ingresar esa cantidad.')
        getAmount()
        
getAmount()

print("Información")
print(f"Nombre: {name}")
print(f"Precio: {price}")
print(f"Cantidad: {amount}")