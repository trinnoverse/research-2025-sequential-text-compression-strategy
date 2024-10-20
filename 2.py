import nltk
from nltk.corpus import wordnet

# Asegúrate de tener WordNet descargado
nltk.download('wordnet')

# Palabras clave con sinónimos más apropiados en contexto
reemplazos = {
    "want": ["wish", "crave"],
    "write": ["draft"],
    "schedule": ["plan"],
    "appointment": ["meet"],
    "doctor": ["MD"],
    "next": ["upcoming"],
    "week": ["7 days"]
}

def reemplazar_sinonimos(frase):
    palabras = frase.split()
    nueva_frase = []

    for palabra in palabras:
        # Limpiar la palabra de puntuación
        palabra_limpia = palabra.strip(",.?!;:")
        sinonimos = []

        # Verificar si la palabra está en el diccionario de reemplazo
        if palabra_limpia.lower() in reemplazos:
            sinonimos = reemplazos[palabra_limpia.lower()]
        else:
            # Buscar sinónimos en WordNet
            for syn in wordnet.synsets(palabra_limpia):
                for lemma in syn.lemmas():
                    if lemma.name() != palabra_limpia:  # Evitar la palabra original
                        sinonimos.append(lemma.name())

        # Elegir un sinónimo más corto que la palabra original
        sinonimo_seleccionado = None
        for sinonimo in sinonimos:
            if len(sinonimo) < len(palabra_limpia):
                sinonimo_seleccionado = sinonimo
                break  # Salir al primer sinónimo que sea más corto

        if sinonimo_seleccionado:
            nueva_frase.append(sinonimo_seleccionado)
        else:
            nueva_frase.append(palabra)  # Si no hay sinónimos más cortos, añade la palabra original

    return ' '.join(nueva_frase)

# Ejemplo de uso
frase_original = "Hello, good morning. I'm writing because I want to schedule an appointment with the doctor next week."
nueva_frase = reemplazar_sinonimos(frase_original)
print("Frase original:", frase_original)
print("Frase con sinónimos más cortos:", nueva_frase)
