import random

def main():
    count = 10
    randint = random.randint(0, 100) 
    
    while count > 0:
        option = int(input(f"Te quedan {count} intentos...\n> "))
        
        n_left = abs(randint - option)
        
        if option == randint:
            print("¡Acertaste!")
            break
        elif n_left > 80:
            print("🧊")
        elif n_left > 60:
            print("CONGELADO")
        elif n_left > 40:
            print("HELADO")
        elif n_left > 20:
            print("FRIO")
        elif n_left > 10:
            print("TIBIO")
        elif n_left > 5:
            print("CALIENTE")
        else:
            print("MUY CALIENTE")
        
        count -= 1
        
    if (count == 0):
        print(f"¡Mejor suerte a la pŕoxima!\nEl resultado era: {randint}")
    
    
main()