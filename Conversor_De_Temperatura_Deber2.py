def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen == "Celsius":
        if unidad_destino == "Fahrenheit":
            return (valor * 9/5) + 32
        elif unidad_destino == "Kelvin":
            return valor + 273.15
        elif unidad_destino == "Rankine":
            return (valor + 273.15) * 9/5
    elif unidad_origen == "Fahrenheit":
        if unidad_destino == "Celsius":
            return (valor - 32) * 5/9
        elif unidad_destino == "Kelvin":
            return (valor - 32) * 5/9 + 273.15
        elif unidad_destino == "Rankine":
            return valor + 459.67
    elif unidad_origen == "Kelvin":
        if unidad_destino == "Celsius":
            return valor - 273.15
        elif unidad_destino == "Fahrenheit":
            return (valor - 273.15) * 9/5 + 32
        elif unidad_destino == "Rankine":
            return valor * 9/5
    elif unidad_origen == "Rankine":
        if unidad_destino == "Celsius":
            return (valor - 491.67) * 5/9
        elif unidad_destino == "Fahrenheit":
            return valor - 459.67
        elif unidad_destino == "Kelvin":
            return valor * 5/9
    return None  # Si no se encuentra una conversión válida

# Ejemplo de uso
valor = float(input("Ingresa el valor de la temperatura: "))
unidad_origen = input("Ingresa la unidad de origen (Celsius, Fahrenheit, Kelvin, Rankine): ")
unidad_destino = input("Ingresa la unidad de destino (Celsius, Fahrenheit, Kelvin, Rankine): ")

resultado = convertir_temperatura(valor, unidad_origen, unidad_destino)
if resultado is not None:
    print(f"{valor} {unidad_origen} son {resultado:.2f} {unidad_destino}")
else:
    print("Conversión no válida. Por favor, verifica las unidades ingresadas.")