qualifications = [10,20,50,60,70,50]

# Colores para el print en consola
RESET = '\033[0m'
BOLD = '\033[01m'

RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
YELLOW = '\033[93m'
LIGHTBLUE = '\033[94m'
LIGHTCYAN = '\033[96m'
 
def printError(x):
    return print(f'{RED}{x}{RESET}\n') 

        
def getAverage(ns):    
    return sum(ns) / len(ns)


def continueFn():
    input(f"Presiona {YELLOW}Enter{RESET} para Continuar...\n")
    
def addNotes():
    global qualifications
    while True:
        try:
            entry = input("Ingresa tus notas (separadas por coma)\n> ")
            print("")
            if not entry:
                print(f"{RED}Debes ingresar al menos 1 calificación.{RESET}\n")
                startProcess()
                return
            qualificationsTemp = list(map(int, entry.split(",")))

            for n in qualificationsTemp:
                if n < 0 or n > 100:
                    raise ValueError("Todas las notas deben estar entre 0 y 100.")

            qualifications = qualificationsTemp
            break
        except ValueError as ve:
            printError(str(ve))
    
def determineApprovalStatus():
    while True:
        try:
            qualification = float(input(f"Ingresa una calificación de la lista: \n{BLUE}{qualifications}{RESET}\n> "))
            print("")
            if qualification not in qualifications:
                raise IndexError
            
            if 0 <= qualification <= 100:
                print(f"El estudiante ha {GREEN + "aprobado" if qualification >= 24 else RED + "reprobado"}{RESET}.\n")
                continueFn()
                break
            else:
                print(f"La calificación debe estar entre {YELLOW}0{RESET} y {YELLOW}100{RESET}\n")
                continue
        except (ValueError, IndexError):
            printError("Valor inválido. Intenta nuevamente.")
            

def getAverage():    
    average = sum(qualifications) / len(qualifications)
    print(f"El promedio es de {YELLOW}{average:.2f}{RESET}\n")
    continueFn()

def countMajorQualifications():
    while True:
        try:
            major = int(input("¿A que valor deben ser mayor las calificaciones?\n> "))
            marginNotes = []
            
            i = 0
            while True:
                if i >= len(qualifications):
                    break
                if qualifications[i] > major:
                    marginNotes.append(qualifications[i])
                i += 1
            
            print(f"\nEstas son las notas mayores a {YELLOW}{major}{RESET} en {BLUE}{qualifications}{RESET}:\n{GREEN}{marginNotes}{RESET}\n")
            continueFn()
            break
        except ValueError:
            print("\nValor inválido. Intentelo nuevamente.\n")
    
def verifySpecificQualification():
    while True:
        try:
            specific = int(input("\nIngresa una calificación específica:\n> "))
            print()
            count = 0
            
            for i in qualifications:
                if i != specific:
                    continue
                    
                count += 1
                print(i)

            if count > 0:
                print(f'\nHay un total de {YELLOW}{count}{RESET} {"números" if count > 1 else "número"} {LIGHTBLUE}"{specific}"{LIGHTBLUE}\n')   
            else:
                print(f'No hay ningún número igual a {YELLOW}{specific}{RESET}.\n')  
                
            continueFn()
            break
        except ValueError:
            print("\nValor inválido. Intentelo nuevamente.\n")

def startProcess():
    global qualifications
    
    while True:
        separator = '=' * len(str(qualifications))
        if len(qualifications) < 1:
            addNotes()
            continue
        
        opcion = input(f"{LIGHTBLUE}{separator}\n{qualifications}\n{separator}{RESET}\n\n{YELLOW}1.{RESET} Determinar estado de aprobación \n{YELLOW}2.{RESET} Calcular promedio\n{YELLOW}3.{RESET} Contar calificaciones mayores que...\n{YELLOW}4.{RESET} Verificar y contar calificaciones específicas\n{YELLOW}5.{RESET} Cambiar calificaciones.\n{YELLOW}6. Salir{RESET}\n> ")
        
        print("")
        
        match opcion:
            case '1':
                determineApprovalStatus()
            case '2':
                getAverage()
            case '3':
                countMajorQualifications()
            case '4':
                verifySpecificQualification()
            case '5':
                qualifications = []
                print()
                continue
            case _:
                printError("\nOpción no válida.\n")
                

startProcess()