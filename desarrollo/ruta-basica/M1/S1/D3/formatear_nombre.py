nombre = ""
segundo_nombre = ""
apellido = ""

def printNamesFormatter(names):
    print(f"\033[32m\n{'='*30} \n {names}\n{'='*30}\033[0m")


def addNames():
    global nombre, segundo_nombre, apellido
    
    variables = ["nombre", "segundo_nombre", "apellido"]
    tipos = ["Nombre", "Segundo Nombre", "Apellido"]
    
    for i, var_name in enumerate(variables):
        valor_actual = globals()[var_name]
        
        if not valor_actual.strip():
            nameInput = input(f"Ingresa tu {tipos[i]}: ").strip()
            globals()[var_name] = nameInput.capitalize()
        else:
            print(f"{tipos[i]} actual: '{valor_actual}'")
    
    return f"{nombre} {segundo_nombre} {apellido}"

def formatear_nombre(name=None, secondName=None, lastName=None):
    global nombre, segundo_nombre, apellido
    
    nombre = ''
    segundo_nombre = '' 
    apellido = ''
    
    if name: nombre = name.title()  # noqa: E701
    if secondName: segundo_nombre = secondName.title()  # noqa: E701
    if lastName: apellido = lastName.title()  # noqa: E701
    
    if not name or not secondName or not lastName:
        print("\033[31mFaltan argumentos, ingresalos manualmente.\033[0m\n")
        return addNames()
    else:
        return f"{nombre.capitalize()} {segundo_nombre.capitalize()} {apellido.capitalize()}"
    
    

print("\n === test #1 === \n")        
printNamesFormatter(formatear_nombre("test"))

print("\n === test #2 === \n")        
printNamesFormatter(formatear_nombre("test", "kasdkask"))

print("\n === test #3 === \n")        
printNamesFormatter(formatear_nombre("Jesus", "de", "Nazaret"))

print("\n === test #4 === \n")  
printNamesFormatter(formatear_nombre())

