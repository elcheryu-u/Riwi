import time
import random

def printColor(msg, color='red'):
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    RESET = '\033[0m'
    
    usedColor = RED
    
    match color:
        case 'green':
            usedColor = GREEN
        case 'blue':
            usedColor = BLUE
        case _:
            usedColor = RED
    
    if isinstance(msg, str):
        print(f"{usedColor}{msg}.{RESET}")


def loading_dots(duration=2):
    start_time = time.time()
    while time.time() - start_time < duration:
        for i in range(duration * 2):
            print(f"{ '|-|'*i}", end='\r')
            time.sleep(.5)
    
    print()

print("Tienes que adivinar un número...\n")

guessMe = random.randint(1, 100)

loading_dots()

attemps = 0

while attemps < 10:
    try:
        guess = int(input('\n\n¿Que número crees que es?\n> '))
        attemps += 1
        
        print(guessMe)
        
        if guess == guessMe:
            pass
        else:
            phrase = f"¡Te pasaste! \nEl número es menor a {guess}" if guess > guessMe else f"Muy por debajo. \nEl número es mayor a {guess}"
            printColor(f"\n\n{phrase}")
            print(f"Te quedan \033[33m{10 - attemps}\033[0m intentos restantes.")
    except ValueError:
        attemps += 1
        printColor("Error: Solo puede contener números enteros.")
        print(f"Te quedan \033[33m{10 - attemps}\033[0m intentos restantes.")
        