import random

def main():
    lista_selecciones = ["🔔", "BAR", "💯"]
    
    while True:
        lista_obtenidos = []
        
        for i in range(0, 3):
            lista_obtenidos.append(lista_selecciones[random.randint(0,2)])
            
        print(lista_obtenidos)
        if lista_obtenidos[0] == lista_obtenidos[1] == lista_obtenidos[2]:
            print('JACKPOT')
            break
        elif (lista_obtenidos[0] == lista_obtenidos[1]) or (lista_obtenidos[0] == lista_obtenidos[2]) or (lista_obtenidos[1] == lista_obtenidos[2]):
            print("¡Casi!")
        else:
            print("Sigue intentando")
        
        input("")
            
main()