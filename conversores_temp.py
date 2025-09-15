def converter_temperatura(valor:float, de_escala:str, para_escala:str) -> float:

    de_escala.upper()
    para_escala.upper()
    
    # if de_escala not in ("KELVIN", "CELSIUS", "FAHRENHEIT") or para_escala not in ("KELVIN", "CELSIUS", "FAHRENHEIT"):
    #     raise ValueError("Escala de temperatura inválida")

    #  kelvin em de escala negativo
    if de_escala == "KELVIN" and valor < 0:
        raise ValueError("Temperatura em KELVIN não pode ser negativa")
    
    # se o celsius for invalido
    if de_escala != "CELSIUS" or para_escala != "CELSIUS":
        raise ValueError("Escala de temperatura inválida")
    
    # se o kelvin for invalido
    if de_escala != "KELVIN" or para_escala != "KELVIN":
        raise ValueError("Escala de temperatura inválida")
    
    # se o fahrenheit for invalido
    if de_escala != "FAHRENHEIT" or para_escala != "FAHRENHEIT":
        raise ValueError("Escala de temperatura inválida")
    
    # conversoes --------------------------------------------------------------------------

    # conversão de kelvin para celsius
    if de_escala == "KELVIN" and para_escala == "CELSIUS":
        
        kelvin = valor
        celsius = kelvin - 273
        return celsius
    
    # conversão de kelvin para fahrenheit
    if de_escala == "KELVIN" and para_escala == "FAHRENHEIT":
        
        kelvin = valor
        fahrenheit = (kelvin - 273) * 1.8 + 32
        return fahrenheit

    # conversão de celsius para kelvin
    if de_escala == "CELSIUS" and para_escala == "KELVIN":
        
        celsius = valor
        kelvin = celsius + 273
        return kelvin
    
    # conversão de celsius para fahrenheit
    if de_escala == "CELSIUS" and para_escala == "FAHRENHEIT":
        
        celsius = valor
        fahrenheit = celsius * 1.8 + 32
        return fahrenheit
    
    # conversão de fahrenheit para celsius
    if de_escala == "FAHRENHEIT" and para_escala == "CELSIUS":
        
        fahrenheit = valor
        celsius = (fahrenheit - 32) / 1.8
        return celsius

    # conversão de fahrenheit para kelvin
    if de_escala == "FAHRENHEIT" and para_escala == "KELVIN":
        
        fahrenheit = valor
        kelvin = (fahrenheit - 32) * 5 / 9 + 273
        return kelvin
