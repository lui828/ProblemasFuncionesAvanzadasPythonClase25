palabras_positivas = ["bien", "genial", "fantástico", "excelente", "feliz"]
palabras_negativas = ["mal", "terrible", "horrible", "malo", "triste"]

def analizar_sentimiento(texto):
    texto = texto.lower()
    conteo_positivo = sum(palabra in texto for palabra in palabras_positivas)
    conteo_negativo = sum(palabra in texto for palabra in palabras_negativas)

    if conteo_positivo > conteo_negativo:
        return "Sentimiento positivo"
    elif conteo_negativo > conteo_positivo:
        return "Sentimiento negativo"
    else:
        return "Sentimiento neutral"

# Ejemplo de uso
texto = input("Escribe una oración para analizar: ")
resultado = analizar_sentimiento(texto)
print(f"El resultado del análisis es: {resultado}")