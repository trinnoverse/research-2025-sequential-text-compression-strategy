import nltk
from nltk.stem import PorterStemmer

# Download NLTK resources if necessary
nltk.download('punkt', quiet=True)

stemmer = PorterStemmer()

def stemming(text: str) -> str:
    """Applies stemming to the input text by reducing words to their root form.
    
    Args:
        text (str): The input string containing words to be stemmed.
        
    Returns:
        str: The stemmed version of the input text.
    """
    words = text.split()
    stemmed_words = [stemmer.stem(word) for word in words]
    return ' '.join(stemmed_words)
