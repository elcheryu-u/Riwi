name = str
price = float
amount = int
discount = int
discountRange = range(101)
totalPrice = float
totalPerUnitPrice = float

# Print de color rojo para hacer más visible el error
def printError(msg):
    RED = '\033[31m'
    RESET = '\033[0m'
    
    if type(msg) == str:
        print(f"{RED}Error: {msg}.{RESET}")

def getName():
    global name
    nameInput = input("Ingresa el nombre del producto:")
    if nameInput.isdigit():
        print('Error, el nombre no puede ser un número')
        getName()
    else:
        name = nameInput

getName()

def getPrice():
    global price
    while True:        
        try:
            priceInput = float(input("Ingresa el valor del producto:"))
            
            if priceInput < 1:
                printError('No se puede ingresar esa cantidad')
                raise TypeError("No negative nums")
            
            price = priceInput
            break
        except TypeError:
            printError('El número no puede ser negativo')
        except ValueError:
            printError('Error, el precio no puede ser un texto')
    
getPrice()

def getAmount():
    global amount
    
    while True:
        try:
            amountInput = int(input("Ingresa la cantidad del producto:"))
            
            if amountInput < 1:
                printError('No se puede ingresar esa cantidad')
                raise TypeError("No negative nums")
            else:
                amount = amountInput
                break     
        except TypeError:
            printError('El número no puede ser negativo')
            
        except ValueError:
            printError('No se puede ingresar esa cantidad')
        
getAmount()

def getDiscount():
    global discount
    global discountRange
    
    while True:
        try:
            discountInput = int(input("Ingresa el porcentaje de descuento:"))
            if discountInput in discountRange:
                discount = discountInput
                break
        except ValueError:
            printError('mal ahi pa, repétilo')

getDiscount()

def getPrice():
    global totalPrice
    global totalPerUnitPrice

    totalPerUnitPrice = price * amount
    discountPrice = totalPerUnitPrice - totalPerUnitPrice * (discount / 100)

    totalPrice = f"{discountPrice:.2f}"

    print(f"Precio total: {price * amount}")
    print(f"Precio con descuento: {discountPrice:.2f}")

getPrice()

print("=====================================")
print(f"Producto:                    {name}")
print(f"------------------------------------")
print(f"Precio:                      {price}")
print(f"Cantidad:                    {amount}")
print(f"Descuento:                   {discount}")
print(f"Total:                       {totalPerUnitPrice}")
print(f"------------------------------------")
print(f"Total a pagar:               {totalPrice}")
print("=====================================")
