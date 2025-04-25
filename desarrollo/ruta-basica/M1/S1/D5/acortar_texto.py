def max_longitud(val, m_length=10):
    return f"{val[:m_length - 3]}..." if len(val) > m_length else val

print(max_longitud(input("Ingresa el texto:"), 4))