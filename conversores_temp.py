def converter_temperatura(valor:float, de_escala:str, para_escala:str) -> float:

# FALTOU FAZER SE AS ESCALAS FOREM IGUAIS
    de_escala = de_escala.upper()
    para_escala = para_escala.upper()
    
    # caso as escalas sejam invalidas
    if de_escala not in ("KELVIN", "CELSIUS", "FAHRENHEIT") or para_escala not in ("KELVIN", "CELSIUS", "FAHRENHEIT"):
        raise ValueError("Escala de temperatura inválida")

    #  kelvin em de escala negativo
    if de_escala == "KELVIN" and valor < 0:
        raise ValueError("Temperatura em KELVIN não pode ser negativa")
    
    # conversoes --------------------------------------------------------------------------

    # conversão de kelvin para celsius
    if de_escala == "KELVIN" and para_escala == "CELSIUS":
        
        kelvin = valor
        celsius = kelvin - 273.15
        return round (celsius, 2)
    
    # conversão de kelvin para fahrenheit
    if de_escala == "KELVIN" and para_escala == "FAHRENHEIT":
        
        kelvin = valor
        fahrenheit = (kelvin - 273.15) * 1.8 + 32
        return round (fahrenheit, 2)

    # conversão de celsius para kelvin
    if de_escala == "CELSIUS" and para_escala == "KELVIN":
        
        celsius = valor
        kelvin = celsius + 273.15
        return round (kelvin, 2) 
    
    # conversão de celsius para fahrenheit
    if de_escala == "CELSIUS" and para_escala == "FAHRENHEIT":
        
        celsius = valor
        fahrenheit = celsius * 1.8 + 32
        return round (fahrenheit, 2) 
    
    # conversão de fahrenheit para celsius
    if de_escala == "FAHRENHEIT" and para_escala == "CELSIUS":
        
        fahrenheit = valor
        celsius = (fahrenheit - 32) / 1.8
        return round (celsius, 2) 

    # conversão de fahrenheit para kelvin
    if de_escala == "FAHRENHEIT" and para_escala == "KELVIN":
        
        fahrenheit = valor
        kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
        return round (kelvin, 2) 
