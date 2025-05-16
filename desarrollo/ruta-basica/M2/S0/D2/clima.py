import urllib.error
import urllib.request
import json
from datetime import datetime

def showCurrentWeather(json_data):
    weather_translation = {
        '200': ("Tormenta", "tormenta eléctrica con lluvia ligera", "11d"),
        '201': ("Tormenta", "tormenta con lluvia", "11d"),
        '202': ("Tormenta", "tormenta eléctrica con fuertes lluvias", "11d"),
        '210': ("Tormenta", "tormenta ligera",  "11d"),
        '211': ("Tormenta", "tormenta",  "11d"),
        '212': ("Tormenta", "fuerte tormenta",  "11d"),
        '221': ("Tormenta", "tormenta irregular",  "11d"),
        '230': ("Tormenta", "tormenta eléctrica con llovizna ligera",  "11d"),
        '231': ("Tormenta", "tormenta eléctrica con llovizna",  "11d"),
        '232': ("Tormenta", "tormenta eléctrica con llovizna intensa",  "11d"),
        '300': ("Llovizna", "llovizna de intensidad ligera", "09d"),
        '301': ("Llovizna", "llovizna", "09d"),
        '302': ("Llovizna", "llovizna de fuerte intensidad", "09d"),
        '310': ("Llovizna", "lluvia ligera y llovizna", "09d"),
        '311': ("Llovizna", "llovizna", "09d"),
        '312': ("Llovizna", "Lluvia lloviznosa de fuerte intensidad", "09d"),
        '313': ("Llovizna", "lluvia y llovizna", "09d"),
        '314': ("Llovizna", "fuertes lluvias y lloviznas", "09d"),
        '321': ("Llovizna", "llovizna de ducha", "09d"),
        '500': ("Lluvia", "", "10d"),
        '501': ("Lluvia", "", "10d"),
        '502': ("Lluvia", "", "10d"),
        '503': ("Lluvia", "", "10d"),
        '504': ("Lluvia", "", "10d"),
        '511': ("Lluvia", "", "13d"),
        '520': ("Lluvia", "", "09d"),
        '521': ("Lluvia", "", "09d"),
        '522': ("Lluvia", "", "09d"),
        '531': ("Lluvia", "", "09d"),
        '600': ("Nieve", "", "13d"),
        '601': ("Nieve", "", "13d"),
        '602': ("Nieve", "", "13d"),
        '611': ("Nieve", "", "13d"),
        '612': ("Nieve", "", "13d"),
        '613': ("Nieve", "", "13d"),
        '615': ("Nieve", "", "13d"),
        '616': ("Nieve", "", "13d"),
        '620': ("Nieve", "", "13d"),
        '621': ("Nieve", "", "13d"),
        '622': ("Nieve", "", "13d"),
        '701': ("Neblina", "neblina", "50d"),
        '711': ("Humo", "humo", "50d"),
        '721': ("Bruma", "bruma", "50d"),
        '731': ("Polvo", "arena/remolinos de polvo", "50d"),
        '741': ("Niebla", "niebla", "50d"),
        '751': ("Arena", "arena", "50d"),
        '761': ("Polvo", "polvo", "50d"),
        '762': ("Ceniza", "Ceniza volcánica", "50d"),
        '771': ("Chubasco", "chubasco", "50d"),
        '781': ("Tornado", "tornado", "50d"),
        '800': ("Despejado", "Cielo despejado", "01d"),
        '801': ("Nubes", "pocas nubes: 11-25%", "02d"),
        '802': ("Nubes", "nubes dispersas: 25-50%", "03d"),
        '803': ("Nubes", "nubes dispersas: 51-84%", "04d"),
        '804': ("Nubes", "nubes cubiertas: 85-100%", "04d"),
    }
            
    weather = json_data["weather"][0]
    sys = json_data["sys"]
    main = json_data["main"]
    
    sys_sunrise = datetime.fromtimestamp(sys["sunrise"]).strftime("%H:%M:%S")
    sys_sunset = datetime.fromtimestamp(sys["sunset"]).strftime("%H:%M:%S")
    
    print(f"El clima en {json_data["name"]} es:")
    print(f"{weather_translation[str(weather["id"])][0]} \n- {weather_translation[str(weather["id"])][1]}", end="\n\n")
    print(f"Temperatura: {main["temp"] - 273.15:.2f}°C")
    print(f"Sensación térmica: {main["feels_like"] - 273.15:.2f}°C")
    print(f"Amanecer: {sys_sunrise} \nAnochecer: {sys_sunset}")
def getCurrentWeather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appId={api_key}"

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            json_data = json.loads(data)
            
            showCurrentWeather(json_data)
    except urllib.error.HTTPError as e:
        errors = {
            '404': "Ciudad no encontrada"
        }
        print(errors[str(e.status)], end="\n")    

def main():
    while True:
        print("""
1. Obtener clima
""")
        option = input("¿Qué deseas hacer?\n> ").strip()
        
        match option:
            case '1':
                city = input("Ciudad\n> ")
                getCurrentWeather(city, "4e749dbf7934114cbc7d67d0e2d560e3")
                
                
main()