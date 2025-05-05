estudiantes = {}


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

def continueFn():
    input(f"Presiona {YELLOW}Enter{RESET} para Continuar...\n")
    

def addStudents():
    
    def getQualifications():
        while True:
            qualifications = tuple(map(int, input(f"Ingrese las notas de {LIGHTBLUE}{name}{RESET}. Separadas por coma y máximo {YELLOW}3{RESET} notas:\n> ").strip().split(',')))
            
            if len(qualifications) > 3:
                print(f"\nMáximo {YELLOW}3{RESET} notas\n")
                continue
            
            if any(i < 0 or i > 5 for i in qualifications):
                print(f"\nLa calificación debe estar entre {YELLOW}0{RESET} y {YELLOW}5{RESET}.\n")
                continue
            
            return qualifications
        
    
    while True:
        try:
            name = input(f"{LIGHTBLUE}¿Como se llama el estudiante?{RESET}\n> ")
            
            qualifications = getQualifications()
            
            estudiantes[name] = qualifications
            
            print(f"¡Perfecto! Se añadio el estudiante {LIGHTBLUE}'{name}'{RESET}.\n")
            break
        except ValueError:
            print("Error")

def showStudentMenu(name):
    while True:
        print(f"{name}")
        option = input(f"""
{YELLOW}1.{RESET} Solicitar datos.
{YELLOW}2.{RESET} Calcular promedio.
{YELLOW}3.{RESET} Aprueba o no aprueba    
===================================    
{YELLOW}4.{RESET} Volver a la lista de estudiantes
{YELLOW}5.{RESET} Volver al menú principal
> 
""")
        print("")
              
        def showStudenData():
            print(f"{name} -> {estudiantes[name]}")
            continueFn()
            
        def calculateAverage(silent=False):
            average = sum(estudiantes[name]) / len(estudiantes[name])
            
            if silent:
                return average
            print(f"El promedio de {LIGHTBLUE}{name}{RESET} es {YELLOW}{average}{RESET}")
            continueFn()
            
        def passOrNotPass():
            average = calculateAverage(True)
            
            print(f"El estudiante {GREEN + "aprobo" if average >= 3 else RED + "reprobo"}{RESET}.\n")
            continueFn()
        
        match option:
            case '1':
                showStudenData()
            case '2':
                calculateAverage()
            case '3':
                passOrNotPass()
            case '4':
                showStudentsListMenu()
            case '5':
                main()
            case _:
                print(f"{RED}Marca una opción valida.{RESET}")
                continueFn()
            
    
    

def showStudentsListMenu():
    print(f"\n{BLUE}¿Qué estudiantes deseas ver?{RESET}\n")
    print(f'{YELLOW}0{RESET}. Volver')
    for i, key in enumerate(estudiantes, start=1):
        print(f"{i}. {key}")
        
    response = int(input('> '))
    
    if response == 0:
        showMenu()
    else:
        for i, key in enumerate(estudiantes, start=1):
            if i == response:
                showStudentMenu(key)
     
def addStudentsMenu():
    while True:
        try:
            amountStudents = int(input(f"{BOLD}{LIGHTBLUE}¿Cuantos estudiantes quieres agregar?{RESET}\n> "))
            
            for i in range(amountStudents):
                addStudents()
            break
        except ValueError:
            print(f"{RED}Ingresa un valor válido.{RESET}")
     
def showMenu():
    option = input(f"""
{BOLD}{LIGHTBLUE}¿Qué deseas hacer?{RESET}

{YELLOW}1.{RESET} Ver estudiantes
{YELLOW}2.{RESET} Añadir estudiantes
{YELLOW}3.{RESET} Salir
""")            
    
    match option:
        case '1':
            showStudentsListMenu()
        case '2':
            addStudentsMenu()
        case '3':
            exit()

def main():
    while True:
        if len(estudiantes) < 1:
            addStudentsMenu()
        else:
            showMenu()
            
        
        
if __name__ == "__main__":
    main()