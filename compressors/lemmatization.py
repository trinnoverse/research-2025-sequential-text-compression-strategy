import nltk
from nltk.stem import WordNetLemmatizer

# Download NLTK resources if necessary
nltk.download('wordnet', quiet=True)

lemmatizer = WordNetLemmatizer()

def lemmatization(text: str) -> str:
    """Lemmatizes the input text by reducing words to their base or root form.
    
    Args:
        text (str): The input string containing words to be lemmatized.
        
    Returns:
        str: The lemmatized version of the input text.
    """
    words = text.split()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(lemmatized_words)
