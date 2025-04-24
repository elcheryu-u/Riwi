def convertir_a_usd():
    salario_cop = float(input("Ingresa el dinero (en COP):"))
    tasa = float(input("Ingresa la tasa de coversion (1USD = ?COP):"))
    
    
    return f"{(salario_cop / tasa):.2f}"
    

print(convertir_a_usd())