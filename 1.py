import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet
import unicodedata
import re

# Descargar recursos necesarios
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Función 1: Eliminar Stop Words
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

# Función 2: Normalización de Texto
def normalize_text(text):
    text = text.lower()
    text = ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

# Función 3: Stemming
def apply_stemming(text):
    ps = PorterStemmer()
    words = word_tokenize(text)
    stemmed_words = [ps.stem(word) for word in words]
    return ' '.join(stemmed_words)

# Función 4: Lematización
def lemmatize_text(text):
    lemmatizer = WordNetLemmatizer()
    words = word_tokenize(text)
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(lemmatized_words)

# Función 5: Reemplazo de Sinónimos
def synonym_replacement(word):
    synonyms = wordnet.synsets(word)
    if synonyms:
        synonym = synonyms[0].lemmas()[0].name()
        return synonym if synonym != word else word
    return word

def replace_synonyms(text):
    words = word_tokenize(text)
    replaced_words = [synonym_replacement(word) for word in words]
    return ' '.join(replaced_words)

# Menú principal para ejecutar funciones
def main():
    print("Selecciona la técnica de NLP que deseas aplicar:")
    print("1. Eliminar Stop Words")
    print("2. Normalización de Texto")
    print("3. Stemming")
    print("4. Lematización")
    print("5. Reemplazo de Sinónimos")

    choice = input("Introduce el número de la técnica: ")
    text = input("Introduce el texto a procesar: ")

    if choice == "1":
        print("Resultado:", remove_stopwords(text))
    elif choice == "2":
        print("Resultado:", normalize_text(text))
    elif choice == "3":
        print("Resultado:", apply_stemming(text))
    elif choice == "4":
        print("Resultado:", lemmatize_text(text))
    elif choice == "5":
        print("Resultado:", replace_synonyms(text))
    else:
        print("Selección inválida")

if __name__ == "__main__":
    main()
