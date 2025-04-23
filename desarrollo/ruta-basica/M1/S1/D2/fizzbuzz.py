for number in range(1, 101):    
    fizz = "Fizz" if number % 3 == 0 else ""
    buzz = "Buzz" if number % 5 == 0 else ""    
    
    print(f"{fizz}{buzz}" if len(fizz) > 0 or len(buzz) > 0 else number)