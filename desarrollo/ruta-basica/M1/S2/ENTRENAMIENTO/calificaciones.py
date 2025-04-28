nota = -1
notas = []
 
printError = lambda x: print(f'\033[31m{x}', end="\033[0m\n") 

def verifyInt(n, restart):
    try:
        return int(n)
    except ValueError:
        printError("El valor no es válido. Tiene que ser un número entero.")
        input("Presiona Enter para Continuar...\n")
        restart()
        
def getAverage(ns):
    sumNotas = 0
    for i in ns:
        sumNotas = sumNotas + i
    
    return sumNotas / len(ns)

def justOne():
    global nota
    
    if nota > -1:
        option = verifyInt(input(f"{"="*25}\nNota: {nota}\n{"="*25}\n1. Evaluar aprobado\n2. Cambiar nota\n3. Volver\n"), justOne)
    
        match option:
            case 1:
                print(f"{"\033[93mNo has aprobado" if nota < 24 else "\033[32mHas aprobado"}", end=".\033[0m\n")
                input("Presiona Enter para Continuar...")
                justOne()
            case 2:
                nota = -1
                justOne()
            case 3:
                startProcess()
            case _:
                printError("Opción no válida.")
                justOne()
    else:
        nota = verifyInt(input("Ingresa tu nota (0/100) "), justOne)
        
        tooBig = nota > 100
        tooSmall = nota < 0

        if tooBig or tooSmall:
            errorMsg = "La nota es demasiado alta.\nNo puede pasar de 100." if tooBig else "La nota es demasiado baja.\nNo puede ser menor a 0."
            printError(errorMsg)
        
        justOne() 

def aLot():
    global notas
    
    def continueFn():
        input("Presiona Enter para Continuar...\n")
        aLot()
    
    if len(notas) > 0:
        notasLength = len(notas)
        print(notasLength)
        option = verifyInt(input(f"{"="*notasLength*3}\n{notas}\n{"="*notasLength*3}\n1. Calcular promedio\n2. Contar calificaciones mayores que...\n3. Verificar y contar calificaciones específicas\n4. Volver\n"), aLot)

        match option:
            case 1:
                promedio = getAverage(notas)
                print(f"El promedio es de {promedio}")
                continueFn()
            case 2:
                margin = verifyInt(input("¿A que valor deben ser mayor las calificaciones? "), aLot)
                marginNotes = []
                
                i = 0
                while True:
                    if i >= len(notas):
                        break
                    if notas[i] > margin:
                        marginNotes.append(notas[i])
                    i += 1
                
                print(f"Estas son las notas mayores a {margin}:\n{marginNotes}")
                continueFn()
            case 3:
                specific = verifyInt(input("Ingresa una calificación específica:"), aLot)
                print('\n')
                count = 0
                
                for i in notas:
                    if i != specific:
                        continue
                        
                    count += 1
                    print(i)
                print(f'Hay un total de {count} números "{specific}"')   
                continueFn()
            case 4:
                startProcess()
            case _:
                printError("Opción no válida.")
                aLot()
                

    else: 
        while True:
            try:
                entrada = input("Ingresa tus notas (separadas por coma)")
                if not entrada:
                    break
                notas = list(map(int, entrada.split(",")))
                aLot()
                break
            except ValueError:
                printError("Ingresa solo números enteros separados por comas.")
            except KeyboardInterrupt: # Para capturar Ctrl+C
                printError("\nInterrupción del usuario. Expresión no evaluada.")
                break
        
def startProcess():
    question = input('\nCon cuantas calificaciones vas a trabajar? [una/muchas] ')

    if (question == "una" or question == "u"):
        justOne()
    elif (question == "muchas" or question == "m"):
        aLot()
    else:
        printError('Valor incorrecto.\nEscoge entre "una" o "muchas"')
        startProcess()

startProcess()

