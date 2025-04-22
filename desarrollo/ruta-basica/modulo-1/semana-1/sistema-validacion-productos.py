name = None
price = None
amount = None
discount = None
discountRange = range(101)
totalPrice = None

def getName():
    global name
    nameInput = input("Ingresa el nombre del producto:")
    if nameInput.isdigit():
        print('Error, el nombre no puede ser un número.')
        getName()
    else:
        name = nameInput

getName()

def getPrice():
    global price
    while True:
        priceInput = input("Ingresa el valor del producto:")
    
        try:
            price = int(priceInput)
            break
        except ValueError:
            try:
                price = float(priceInput)
                break
            except ValueError:
                print('Error, el precio no puede ser un texto.')
    
getPrice()

def getAmount():
    global amount
    amountInput = input("Ingresa la cantidad del producto:")
    
    try:
        if amount < 1:
            print('No se puede ingresar esa cantidad.')
            getAmount()
        else:
            amount = int(amountInput)
    except ValueError:
        print('No se puede ingresar esa cantidad.')
        getAmount()
        
getAmount()

def getDiscount():
    global discount
    global discountRange

    discountInput = int(input("Ingresa el porcentaje de descuento:"))

    if discountInput in discountRange:
        discount = discountInput
    else:
        print('mal ahi pa, repétilo')
        getDiscount()

getDiscount()

def getPrice():
    global totalPrice

    totalPerUnitPrice = price * amount
    discountPrice = totalPerUnitPrice - totalPerUnitPrice * (discount / 100)

    totalPrice = f"{discountPrice:.2f}"

    print(f"Precio total: {price * amount}")
    print(f"Precio con descuento: {discountPrice:.2f}")

getPrice()

print("=====================================")
print(f"Producto                     {name} \n")
print(f"Precio:                      {price}")
print(f"Cantidad:                    {amount}")
print(f"Descuento:                   {discount}")
print(f"Precio Total:                {totalPrice}")
print("=====================================")
