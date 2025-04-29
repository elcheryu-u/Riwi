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
    return sum(ns) / len(ns)


def continueFn(fn):
    input("Presiona Enter para Continuar...\n")
    fn()

def justOne():
    global nota
    
    if nota > -1:
        try:
            option = verifyInt(input(f"{'='*25}\nNota: {nota}\n{'='*25}\n1. Evaluar aprobado\n2. Cambiar nota\n3. Volver\n> "), justOne)
    
            match option:
                case 1:
                    mensaje = "\033[93mNo has aprobado" if nota < 24 else "\033[32mHas aprobado"
                    print(f"{mensaje}.", end="\033[0m\n")
                    continueFn(justOne)
                case 2:
                    nota = -1
                    justOne()
                case 3:
                    startProcess()
                case _:
                    printError("Opción no válida.")
                    justOne()
        except (KeyboardInterrupt, EOFError):
            printError("Interrupción detectada. Regresando al menú.")
            startProcess()
    else:
        try:
            n = input("Ingresa tu nota (0/100): ")
            n = verifyInt(n, justOne)
        
            tooBig = n > 100
            tooSmall = n < 0

            if tooBig or tooSmall:
                errorMsg = "La nota es demasiado alta.\nNo puede pasar de 100." if tooBig else "La nota es demasiado baja.\nNo puede ser menor a 0."
                printError(errorMsg)
                justOne() 
                return
            
            nota = n
            justOne()
        except (KeyboardInterrupt, EOFError):
            printError("Interrupción detectada. Regresando al menú")
            startProcess()

def aLot():
    global notas
    
    if len(notas) > 0:
        separator = '='*30
        try:
            option = verifyInt(input(f"{separator}\n{notas}\n{separator}\n1. Calcular promedio\n2. Contar calificaciones mayores que...\n3. Verificar y contar calificaciones específicas\n4. Cambiar calificaciones.\n5. Volver\n> "), aLot)

            match option:
                case 1:
                    promedio = getAverage(notas)
                    print(f"\nEl promedio es de {promedio:.2f}")
                    continueFn(aLot)
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
                    
                    print(f"\nEstas son las notas mayores a {margin}:\n{marginNotes}")
                    continueFn(aLot)
                case 3:
                    specific = verifyInt(input("\nIngresa una calificación específica:"), aLot)
                    print()
                    count = 0
                    
                    for i in notas:
                        if i != specific:
                            continue
                            
                        count += 1
                        print(i)

                    if count > 0:
                        print(f'\nHay un total de {count} números "{specific}"')   
                    else:
                        print(f'No hay ningún número igual a "{specific}".')  
                    continueFn(aLot)
                case 4:
                    notas = []
                    print()
                    aLot()
                case 5:
                    startProcess()
                case _:
                    printError("Opción no válida.")
                    aLot()
        except (KeyboardInterrupt, EOFError):
            printError("Interrupción detectada. Regresando al menú.")
            startProcess()
    else: 
        while True:
            try:
                entrada = input("Ingresa tus notas (separadas por coma)\n> ")
                if not entrada:
                    startProcess()
                    return
                notasTemp = list(map(int, entrada.split(",")))

                for n in notasTemp:
                    if n < 0 or n > 100:
                        raise ValueError("Todas las notas deben estar entre 0 y 100.")

                notas = notasTemp
                aLot()
                break
            except ValueError as ve:
                printError(str(ve))
            except (KeyboardInterrupt, EOFError):
                printError("\nInterrupción del usuario. Expresión no evaluada.")
                startProcess()
                break
        
def startProcess():
    try:
        question = input('\nCon cuantas calificaciones vas a trabajar? [una/muchas] ')

        if question.lower() in ("una", "u"):
            justOne()
        elif question.lower() in ("muchas", "m"):
            aLot()
        else:
            printError('Valor incorrecto.\nEscoge entre "una" o "muchas"')
            startProcess()
    except (KeyboardInterrupt, EOFError):
        printError("Interrupción detectada. Cerrando programa.")
        exit()

startProcess()

